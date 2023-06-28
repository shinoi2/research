import logging

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
        return jsonify({
            "msg": "ok",
            "code": 0,
            "name": "",
            "phone": "",
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

    return jsonify({
        "msg": "ok",
        "code": 0,
        "name": name,
        "phone": phone,
        "waybill": code128["data"]
    })

def sf_express_ocr(image):
    ocr_result_list = ocr_client.predict(image)
    ocr_results = list(map(lambda x: x["label"], ocr_result_list))
    phone = ""
    name = ""
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    def isChinese(string):
        for ch in string:
            if u'\u4e00' <= ch <= u'\u9fff':
                return True
        return False
    def isPhone(result):
        if result[0] == '1' and all(r in numbers for r in result[-4:]):
            if len(result) == 6 and result[-5] in ['*', '+']:
                return True
            elif len(result) == 5:
                return True
        return False
    logger.info(ocr_results)
    ocr_results = list(filter(lambda x: isChinese(x) or isPhone(x), ocr_results))
    for i, result in enumerate(ocr_results):
        if isPhone(result):
            phone = result[-4:]
            if (i + 1 < len(ocr_results) and len(ocr_results[i+1]) <= 10):
                name = ocr_results[i+1]
            if isChinese(ocr_results[i]):
                name = ""
                for ch in ocr_results[i]:
                    if u'\u4e00' <= ch <= u'\u9fff':
                        name += ch
                    else:
                        break
            if (i > 0 and len(ocr_results[i-1]) <= 10):
                name = ocr_results[i-1]
            break
        if (len(result) <= 4 and
            result[0] == '收'):
            name = result
    if len(name) >= 1 and name[0] == '收':
        name = name[1:]
    return name, phone


# if __name__ == "__main__":
#     image = cv2.imread("/home/pji/快递单/IMG_7527.HEIC.JPG.JPG")
#     sf_express(image)