import cv2
from common import get_image_v2
from flask import jsonify
from . import face_bp
from . import face_recognition_client

@face_bp.route('/detector', methods=['POST'])
def detector():
    image = get_image_v2()
    if image is None:
        return jsonify({
            "msg": "image 或 url 参数不存在",
            "code": 1,
        })
    image = cv2.imencode('.jpg', image)[1].tostring()
    count, result = face_recognition_client.detect(image=image)

    def format_data(count, result):
        return {
            "msg": "OK",
            "code": 0,
            "count": count,
            "data": result
        }

    return jsonify(format_data(count, result))
