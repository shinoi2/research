import cv2
from .proto import object_pb2_grpc, object_pb2
import grpc
import numpy as np

class ObjectDetectionClient:
    def __init__(self, url = 'object_detection:50053') -> None:
        channel = grpc.insecure_channel(url)
        self.client = object_pb2_grpc.ObjectServiceStub(channel=channel)
    def predict(self, image):
        image = cv2.imencode('.jpg', image)[1].tobytes()
        request = object_pb2.ObjectRequest(image = image)
        responses = self.client.predict(request)
        data = []
        for response in responses.responses:
            data.append({
                "label": response.label,
                "score": float(response.score),
                "rect":{
                    "left": float(response.rect.left),
                    "top": float(response.rect.top),
                    "right": float(response.rect.right),
                    "bottom": float(response.rect.bottom)
                }
            })
        return data



# if __name__ == "__main__":
#     with open("./light.jpg", "rb") as f:
#         image = f.read()
#     conn = grpc.insecure_channel('localhost:50052')
#     client = light_pb2_grpc.LightServiceStub(channel=conn)
#     request = light_pb2.LightRequest(images=[image])
#     response = client.predict(request)
#     print(response)
