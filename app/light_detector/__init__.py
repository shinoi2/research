# from .light_client import LightDetectionClient
from paddle_serving_client import Client
from paddle_serving_app.reader import DetectionSequential, \
    DetectionResize, \
    DetectionNormalize, \
    DetectionTranspose
import numpy as np

class LightDetectionClient:
    def __init__(self, url= 'light_detection:9392', thresholds = 0.5):
        self.preprocess = DetectionSequential([
            DetectionResize(
                (608, 608), False, interpolation=2),
            DetectionNormalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225], True),
            DetectionTranspose((2, 0, 1)),
        ])
        self.client = Client()
        self.thresholds = thresholds
        self.client.load_client_config("./light_detector/light_client/serving_client_conf.prototxt")
        if isinstance(url, str):
            self.client.connect([url])
        if isinstance(url, list):
            self.client.connect(url)

    def predict(self, image):
        im, im_info = self.preprocess(image)
        fetch_map = self.client.predict(
            feed={
                "image": im,
                "im_shape": im_info["im_shape"],
                "scale_factor": im_info["scale_factor"],
            },
            fetch=["multiclass_nms3_0.tmp_0"],
            batch=False)
        result = []
        if fetch_map['multiclass_nms3_0.tmp_0'][0][0] != -1.0:
            for data in fetch_map["multiclass_nms3_0.tmp_0"]:
                if float(data[1]) <= self.thresholds:
                    continue
                result.append({
                    "score": float(data[1]),
                    "rect":{
                        "left": float(data[2]),
                        "top": float(data[3]),
                        "right": float(data[4]),
                        "bottom": float(data[5])
                    }
                })
        return result
