import grpc
from .proto import plate_pb2, plate_pb2_grpc
import cv2

class PlateDetectionClient:
    def __init__(self, url = 'plate_detection:50053') -> None:
        channel = grpc.insecure_channel(url)
        self.client = plate_pb2_grpc.PlateServiceStub(channel = channel)
    def predict(self, image):
        img = cv2.imencode('.jpg', image)[1].tobytes()
        request = plate_pb2.PlateRequest(image=img)
        responses = self.client.predict(request)
        data = []
        for response in responses.Plates:
            width = float(response.rect.right) - float(response.rect.left)
            height = float(response.rect.bottom) - float(response.rect.top)
            data.append({
                "score" : float(response.score),
                "rect" : {
                    "left" : max((float(response.rect.left) - 0.1*width), 0),
                    "top" : max((float(response.rect.top) - 0.1*height), 0),
                    "right" : min((float(response.rect.right) + 0.1*width), image.shape[1]),
                    "bottom" : min((float(response.rect.bottom) + 0.1*height), image.shape[1])
                },
                "point" : {
                    "topleft" :
                    {
                        "x" : float(response.points.topleft.x),
                        "y" : float(response.points.topleft.y)
                    } ,
                    "topright" :
                    {
                        "x" : float(response.points.topright.x),
                        "y" : float(response.points.topright.y)
                    } ,
                    "bottomleft" :
                    {
                        "x" : float(response.points.bottomleft.x),
                        "y" : float(response.points.bottomleft.y)
                    } ,
                    "bottomright" :
                    {
                        "x" : float(response.points.bottomright.x),
                        "y" : float(response.points.bottomright.y)
                    } ,
                }
            })
        return data