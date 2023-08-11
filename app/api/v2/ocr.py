import logging
import re
from datetime import datetime
import uuid

import cv2
import numpy as np
from flask import jsonify

from common import get_image_v2
from ocr_recongnition import OCRClient
from qrcode import QRCodeClient

from . import v2_bp

ocr_client = OCRClient()
qrcode_client = QRCodeClient()
logger = logging.getLogger('gunicorn.error')

@v2_bp.route('/ocr', methods=['POST'])
def ocr():
    image = get_image_v2()
    if image is None:
        return jsonify({
            "msg": "image 或 url 参数不存在",
            "code": 1
        })
    result = ocr_client.predict(image)
    def format_data(result):
        count = len(result)
        return {
            "msg": "OK",
            "code": 0,
            "count": count,
            "data": result
        }

    return jsonify(format_data(result))

@v2_bp.route('/ocr/qrcode', methods=['POST'])
def qrcode():
    image = get_image_v2()
    if image is None:
        return jsonify({
            "msg": "image 或 url 参数不存在",
            "code": 1
        })
    result = qrcode_client.predict(image=image)
    def format_data(result):
        count = len(result)
        return {
            "msg": "OK",
            "code": 0,
            "count": count,
            "data": result
        }

    return jsonify(format_data(result))

@v2_bp.route('/ocr/sf_express', methods=['POST'])
def sf_express():
    image = get_image_v2()
    if image is None:
        return jsonify({
            "msg": "image 或 url 参数不存在",
            "code": 1
        })
    qrcode_result_list = qrcode_client.predict(image)
    code128 = None
    qrcode = None
    for qrcode_result in qrcode_result_list:
        if qrcode_result["type"] == "CODE128" and qrcode_result["data"][:2] == "SF":
            code128 = qrcode_result
        elif qrcode_result["type"] == "QRCODE" and qrcode_result["data"][:4] == "MMM=":
            qrcode = qrcode_result
    if not code128:
        if qrcode:
            try:
                code128 = {
                    "data": eval(qrcode["data"][4:])['k5']
                }
            except Exception:
                return jsonify({
                    "msg": "识别失败",
                    "code": 2
                })
        else:
            return jsonify({
                "msg": "识别失败",
                "code": 2
            })
    if not qrcode:
        # naive
        name, phone = sf_express_ocr(image)

        return jsonify({
            "msg": "ok",
            "code": 0,
            "name": name,
            "phone": phone,
            "waybill": code128["data"]
        })

    # 透视变化转换
    pts1 = np.float32([
        [qrcode["polygon"]["top-left"]["x"], qrcode["polygon"]["top-left"]["y"]],
        [qrcode["polygon"]["top-right"]["x"], qrcode["polygon"]["top-right"]["y"]],
        [qrcode["polygon"]["bottom-right"]["x"], qrcode["polygon"]["bottom-right"]["y"]],
        [qrcode["polygon"]["bottom-left"]["x"], qrcode["polygon"]["bottom-left"]["y"]],
    ])
    pts2 = np.float32([
        [720, 20],
        [980, 20],
        [980, 280],
        [720, 280],
    ])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    new_image = cv2.warpPerspective(image, matrix, (1000, 300))
    name, phone = sf_express_ocr(new_image)

    if name == "" and phone == "":
        # v2
        pts2 = np.float32([
            [520, 320],
            [520+260, 320],
            [520+260, 320+260],
            [520, 320+260],
        ])
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        new_image = cv2.warpPerspective(image, matrix, (800, 300))
        name, phone = sf_express_ocr(new_image)

    if name == "" and phone == "":
        # naive
        name, phone = sf_express_ocr(image)

    return jsonify({
        "msg": "ok",
        "code": 0,
        "name": name,
        "phone": phone,
        "waybill": code128["data"]
    })

def sf_express_ocr(image):
    ocr_result_list = ocr_client.predict(image)
    path = f"/tmp/{uuid.uuid4()}.jpg"
    cv2.imwrite(path, image)
    ocr_results = list(map(lambda x: x["label"], ocr_result_list))
    logger.info(f"{path}: {ocr_results}")
    ocr_boxes = list(map(lambda x: x["polygon"], ocr_result_list))
    phone = ""
    name = ""
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    zh = ["　", "！", "＂", "＃", "＄", "％", "＆", "＇", "（", "）",
          "＊", "＋", "，", "－", "．", "／", "：", "；", "＜", "＝",
          "＞", "？", "＠", "［", "＼", "］", "＾", "＿", "｀", "｛",
          "｜", "｝", "～"]
    en = [" ", "!", "\"", "#", "$", "%", "&", "'", "(", ")",
          "*", "+", ",", "-", ".", "/", ":", ";", "<", "=",
          ">", "?", "@", "[", "\\", "]", "^", "_", "`", "{",
          "|", "}", "~"]
    def replaceZhOp(string):
        for z, e in zip(zh, en):
            string = string.replace(z, e)
        return string
    def isPhone(result):
        # 支持的格式
        # 17890
        regex = re.compile(r'1\d{4}$')
        match = regex.match(result)
        if bool(match):
            return True
        # 1*7890
        # 1****7890
        # 189****7890
        # 中间的特殊
        regex = re.compile(r'(\d|\d{3})[\*\+x×#]{1,4}\d{4}$')
        match = regex.match(result)
        if bool(match):
            return True
        # *7890
        # ***7890
        regex = re.compile(r'[\*\+x×#]{1,4}\d{4}$')
        match = regex.match(result)
        if bool(match):
            return True
        # 18912347890
        regex = re.compile(r'\d{11}$')
        match = regex.match(result)
        if bool(match):
            return True
    def getCenter(box):
        return (
            (box["bottom-left"]["x"] + box["bottom-right"]["x"] + box["top-left"]["x"] + box["top-right"]["x"]) / 4,
            (box["bottom-left"]["y"] + box["bottom-right"]["y"] + box["top-left"]["y"] + box["top-right"]["y"]) / 4
        )
    def len_v(v):
        return (v["x"] ** 2 + v["y"] ** 2) ** 0.5
    def cos_2v(v1, v2):
        return (v1["x"] * v2["x"] + v1["y"] * v2["y"]) / len_v(v1) / len_v(v2)
    def vector(p1, p2):
        return {
            "x": p2["x"] - p1["x"],
            "y": p2["y"] - p1["y"],
        }
    def cos_3p(p1, p2, p3):
        return cos_2v(vector(p1, p2), vector(p2, p3))
    def isLeft(c1, c2):
        return (cos_3p(c1["top-left"], c1["top-right"], c2["top-left"]) >= 0.5 and
            cos_3p(c1["top-left"], c1["top-right"], c2["top-left"]) >= 0.5 and
            cos_3p(c1["top-left"], c1["top-right"], c2["top-left"]) >= 0.5 and
            cos_3p(c1["top-left"], c1["top-right"], c2["top-left"]) >= 0.5)
    def distance(c1, c2):
        return (c1[0]-c2[0])**2 + (c1[1]-c2[1])**2
    def findName(index, ocr_results, ocr_boxes):
        center = getCenter(ocr_boxes[index])
        min_dis = 0x3f3f3f3f
        min_index = -1
        for i, box in enumerate(ocr_boxes):
            if i != index:
                c = getCenter(box)
                if isLeft(box, ocr_boxes[index]) and (distance(c, center) < min_dis):
                    min_dis = distance(c, center)
                    min_index = i
        return ocr_results[min_index]
    ocr_results = list(map(replaceZhOp, ocr_results))
    for i, result in enumerate(ocr_results):
        if isPhone(result):
            phone = result[-4:]
            if u'\u4e00' <= result[0] <= u'\u9fff':
                name = ""
                for ch in ocr_results[i]:
                    if u'\u4e00' <= ch <= u'\u9fff':
                        name += ch
            else:
                name = findName(i, ocr_results, ocr_boxes)
            break
    if len(name) >= 1 and name[0] == '收':
        name = name[1:]
    return name, phone


# if __name__ == "__main__":
#     image = cv2.imread("/home/pji/快递单/IMG_7527.HEIC.JPG.JPG")
#     sf_express(image)