import grpc
import sys
sys.path.append('/home/pji/workspace/HyperLPR/Prj-Linux/hyperlpr/build')
from pji.protos import lpr_pb2
from pji.protos import lpr_pb2_grpc

def readfile(image):
    with open(image, 'rb') as f:
        return f.read()


class PlateClient:
    def __init__(self, url='plate_detection:1234') -> None:
        channel = grpc.insecure_channel(url)
        self.client = lpr_pb2_grpc.LicenseRecognitionEngineStub(channel)
    
    def recongition(self, image):
        request = lpr_pb2.Request()
        request.image = image
        response = self.client.Recognition(request)
        results = []
        for plate in response.plates:
            if plate.score < 0.75:
                continue
            results.append({
                "license": plate.license,
                "score": plate.score,
                "rect": {
                    "bottom": plate.rect.bottom,
                    "top": plate.rect.top,
                    "left": plate.rect.left,
                    "right": plate.rect.right
                }
            })
        return results
