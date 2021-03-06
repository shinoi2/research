import cv2
from common import get_image_v2
from flask import jsonify
from . import v2_bp
from face_recognition import FaceRecognitionClient
from mask_detector import MaskDetector

face_recognition_client = FaceRecognitionClient()
mask_detector = MaskDetector()
@v2_bp.route('/mask', methods=['POST'])
def mask():
    image = get_image_v2()
    if image is None:
        return jsonify({
            "msg": "image 或 url 参数不存在",
            "code": 1
        })
    img = cv2.imencode('.jpg', image)[1].tostring()
    count, results = face_recognition_client.detect(image=img)
    data = []
    mask_count = no_mask_count = 0
    if results:
        images = []
        rect = []
        for  i, result in enumerate(results):
            rect.append(result['rect'])
            images.append(image[int(rect[i]['top'] - 1):int(rect[i]['bottom'] + 1), int(rect[i]['left'] - 1):int(rect[i]['right'] + 1)])
        results= mask_detector.predict(images=images)
        for i, result in enumerate(results):
            data.append({
                    "score": result['score'],
                    "rect": rect[i],
                    "mask": result['mask'],
                })
            if result['mask'] == True:
                mask_count += 1
            else:
                no_mask_count += 1
    def format_data(data, mask_count, no_mask_count):
        count = len(data)
        return {
            "msg": "OK",
            "code": 0,
            "count": count,
            "mask_count": mask_count,
            "no_mask_count": no_mask_count,
            "data": data,
        }

    return jsonify(format_data(data, mask_count, no_mask_count))
