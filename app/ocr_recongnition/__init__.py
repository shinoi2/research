import base64
import json

import cv2
import requests


class OCRClient:
    def __init__(self, host: str="ocr_recongnition", port: int=9998) -> None:
        self.url = f"http://{host}:{port}/ocr/prediction"

    @staticmethod
    def cv2_to_base64(image):
        return base64.b64encode(cv2.imencode('.jpg', image)[1]).decode(
            'utf8')  #data.tostring()).decode('utf8')

    def predict(self, image_data:str):
        image = self.cv2_to_base64(image_data)
        data = {"key": ["image"], "value": [image]}
        res = requests.post(url=self.url, data=json.dumps(data)).json()
        if res["err_no"] == 0:
            res_list = eval(res["value"][0])
            result = []
            for r in res_list:
                result.append({
                    "label": r[0][0],
                    "score": float(r[0][1]),
                    "polygon": {
                        "top-left": {
                            "x": r[1][0][0],
                            "y": r[1][0][1],
                        },
                        "top-right": {
                            "x": r[1][1][0],
                            "y": r[1][1][1],
                        },
                        "bottom-right": {
                            "x": r[1][2][0],
                            "y": r[1][2][1],
                        },
                        "bottom-left": {
                            "x": r[1][3][0],
                            "y": r[1][3][1],
                        },
                    }
                })
            return result
        else:
            return []
