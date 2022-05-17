from paddle_serving_client import Client
from paddle_serving_app.reader import DetectionSequential, \
    DetectionResize, \
    DetectionNormalize, \
    DetectionTranspose

class FaceDetector:
    def __init__(self, url= 'face_detection:9395', thresholds = 0.5):
        self.preprocess = DetectionSequential([
            DetectionResize(
                (1024, 1024), False, interpolation=2),
            DetectionNormalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225], True),
            DetectionTranspose((2, 0, 1)),
        ])
        self.client = Client()
        self.thresholds = thresholds
        self.client.load_client_config("./face_detector/lite_face_client/serving_client_conf.prototxt")
        if isinstance(url, str):
            self.client.connect([url])
        if isinstance(url, list):
            self.client.connect(url)

    def predict(self, image):
        im, _ = self.preprocess(image)
        fetch_map = self.client.predict(
            feed={
                "image": im,
            },
            fetch=["save_infer_model/scale_0"],
            batch=False)
        result = []
        image_h = image.shape[0]
        image_w = image.shape[1]
        if fetch_map['save_infer_model/scale_0'][0][0] != -1.0: 
            for data in fetch_map['save_infer_model/scale_0']:
                if float(data[1]) <= self.thresholds:
                    continue
                result.append({
                    "score": float(data[1]),
                    "rect":{
                        "left": float(max(data[2]*image_w, 0)),
                        "top": float(max(data[3]*image_h, 0)),
                        "right": float(max(data[4]*image_w, 0)),
                        "bottom": float(max(data[5]*image_h, 0))
                    }
                })


        return result
