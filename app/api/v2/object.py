from socket import MsgFlag
from object_detector import ObjectDetectionClient
from common import get_image_v2
from flask import jsonify
from . import v2_bp

object_detector = ObjectDetectionClient()
@v2_bp.route('/object', methods=['POST'])
def object():
    image = get_image_v2()
    if image is None:
        return jsonify({
            "msg": "image 或 url 参数不存在",
            "code": 1
        })
    result = object_detector.predict(image)

    def format_data(result):
        return {
            "msg": "OK",
            "code": 0,
            "data": result
        }
    return jsonify(format_data(result))
