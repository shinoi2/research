from plate_detector import PlateDetectionClient, LprnetDetectionClient
from common import get_image_v2
from flask import jsonify
from . import v2_bp
import cv2
import numpy as np

def ImageProcess(image, point):
    topleft_x = max((point["topleft"]["x"] - (point["topright"]["x"] - point["topleft"]["x"])*0.1), 0)
    topleft_y = max((point["topleft"]["y"] - (point["bottomleft"]["y"] - point["topleft"]["y"])*0.1), 0)
    bottomleft_x = max((point["bottomleft"]["x"] - (point["bottomright"]["x"] - point["bottomleft"]["x"])*0.1), 0)
    bottomleft_y = min((point["bottomleft"]["y"]+ (point["bottomleft"]["y"] - point["topleft"]["y"])*0.1), image.shape[0])
    topright_x = min((point["topright"]["x"] + (point["topright"]["x"] - point["topleft"]["x"])*0.1), image.shape[1])
    topright_y = max((point["topright"]["y"] - (point["bottomright"]["y"] - point["topright"]["y"])*0.1), 0)
    bottomright_x = min((point["bottomright"]["x"] + (point["bottomright"]["x"] - point["bottomleft"]["x"])*0.1), image.shape[1])
    bottomright_y = min((point["bottomright"]["y"] + (point["bottomright"]["y"] - point["topright"]["y"])*0.1), image.shape[0])
    pts_o = np.float32([[topleft_x, topleft_y], [topright_x, topright_y], [bottomleft_x, bottomleft_y], [bottomright_x, bottomright_y]])
    top = min(topleft_y, topright_y)
    bottom = max(bottomleft_y, bottomright_y)
    left = min(topleft_x, bottomleft_x)
    right = max(topright_x, bottomright_x)
    pts_d = np.float32([[left, top], [right, top], [left, bottom], [right, bottom]])
    img = cv2.getPerspectiveTransform(pts_o, pts_d)
    img = cv2.warpPerspective(image, img, (image.shape[1], image.shape[0]))
    img = img[int(top):int(bottom), int(left):int(right)]
    return img

plate_detector = PlateDetectionClient()
lprnet_recognition = LprnetDetectionClient()
@v2_bp.route('/vlpr', methods=['POST'])
def vlpr():
    image = get_image_v2()
    if image is None:
        return jsonify({
            "msg": "image 或 url 参数不存在",
            "code": 1
        })
    results = plate_detector.predict(image = image)
    data = []
    if len(results):
        rect = []
        score = []
        images = []
        for result in results:
            score.append(result["score"])
            rect.append(result["rect"])
            img = ImageProcess(image, result["point"])
            images.append(img)
        results = lprnet_recognition.predict(images = images)
        for i, result in enumerate(results):
            data.append({
                "license" : result,
                "score" : score[i],
                "rect" : rect[i]
            })

    def format_data(data):
        return {
            "code": 0,
            "msg": "OK",
            "count": len(data),
            "data": data
        }

    return jsonify(format_data(data))

