import cv2
import numpy as np
from pyzbar import pyzbar


class QRCodeClient:
    def __init__(self) -> None:
        depro = './qrcode/wechatcv/detect.prototxt'
        decaf = './qrcode/wechatcv/detect.caffemodel'
        srpro = './qrcode/wechatcv/sr.prototxt'
        srcaf = './qrcode/wechatcv/sr.caffemodel'
        self.wechat_detect = cv2.wechat_qrcode_WeChatQRCode(depro, decaf, srpro, srcaf)

    def wechat_det(self, image):
        qrcodes, points = self.wechat_detect.detectAndDecode(image)
        result = []
        for i in range(len(qrcodes)):
            result.append({
                "type": "QRCODE",
                "data": qrcodes[i],
                "polygon": {
                    "top-left": {
                        "x": float(points[i][0][0]),
                        "y": float(points[i][0][1]),
                    },
                    "top-right": {
                        "x": float(points[i][1][0]),
                        "y": float(points[i][1][1]),
                    },
                    "bottom-right": {
                        "x": float(points[i][2][0]),
                        "y": float(points[i][2][1]),
                    },
                    "bottom-left": {
                        "x": float(points[i][3][0]),
                        "y": float(points[i][3][1]),
                    },
                }
            })
        return result

    def pyzbar_det(self, image):
        res_list = pyzbar.decode(image)
        result = []
        for res in res_list:
            if res.type == "QRCODE":
                continue
            result.append({
                "type": res.type,
                "data": res.data.decode(),
                "polygon": {
                    "top-right": {
                        "x": res.polygon[0].x,
                        "y": res.polygon[0].y,
                    },
                    "top-left": {
                        "x": res.polygon[1].x,
                        "y": res.polygon[1].y,
                    },
                    "bottom-right": {
                        "x": res.polygon[2].x,
                        "y": res.polygon[2].y,
                    },
                    "bottom-left": {
                        "x": res.polygon[3].x,
                        "y": res.polygon[3].y,
                    },
                } if len(res.polygon) >= 4 else {}
            })
        return result

    def predict(self, image):
        return self.wechat_det(image) + self.pyzbar_det(image)


if __name__ == "__main__":
    client = QRCodeClient()
    with open("/home/pji/test2.jpg", 'rb') as file:
        image_data = file.read()
        image = cv2.imdecode(np.frombuffer(image_data, np.uint8), cv2.IMREAD_COLOR)
        res = client.predict(image)
        for r in res:
            print(r)