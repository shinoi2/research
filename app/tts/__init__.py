import requests
import uuid
import json
import base64
import soundfile
import io


class TTSClient:
    def __init__(self, host: str="speech_server", port: int=8090):
        self.url = f'http://{host}:{port}/paddlespeech/tts'

    def __call__(self,
                 input: str,
                 spk_id: int=0,
                 speed: float=1.0,
                 volume: float=1.0,
                 sample_rate: int=16000):
        request = {
            "text": input,
            "spk_id": spk_id,
            "speed": speed,
            "volume": volume,
            "sample_rate": sample_rate,
        }
        res = requests.post(self.url, json.dumps(request))
        response_dict = res.json()
        outfile = f'/tmp/{uuid.uuid4()}.wav'
        wav_base64 = response_dict["result"]["audio"]
        audio_data_byte = base64.b64decode(wav_base64)
        samples, sample_rate = soundfile.read(io.BytesIO(audio_data_byte), dtype='float32')
        soundfile.write(outfile, samples, sample_rate)
        return outfile
