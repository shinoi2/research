from plate_detector import PlateClient
from common import get_image_v2
from flask import jsonify
from . import v2_bp
import cv2

plate_detector = PlateClient()
@v2_bp.route('/vlpr', methods=['POST'])
def vlpr():
    image = get_image_v2()
    if image is None:
        return jsonify({
            "msg": "image 或 url 参数不存在",
            "code": 1
        })
    image = cv2.imencode('.jpg', image)[1].tostring()
    results = plate_detector.recongition(image)

    def format_data(data):
        return {
            "code": 0,
            "msg": "OK",
            "count": len(data),
            "data": data
        }

    return jsonify(format_data(results))

