from urllib.error import HTTPError
import ffmpeg
import requests
import json
import uuid
import base64
import os

class ASRClient:
    def __init__(self, host: str="speech_server", port: int=8090):
        self.asr_url = f'http://{host}:{port}/paddlespeech/asr'
        self.text_url = f'http://{host}:{port}/paddlespeech/text'

    def __call__(self, audio_bytes):
        wav_file = f"/tmp/{uuid.uuid4()}.wav"
        process = (
            ffmpeg
            .input('pipe:')
            .output(wav_file, acodec='pcm_s16le', ar=16000)
            .overwrite_output()
            .run_async(pipe_stdin=True)
        )
        process.communicate(input=audio_bytes)
        if not os.path.exists(wav_file):
            raise FileNotFoundError()
        with open(wav_file, 'rb') as f:
            base64_bytes = base64.b64encode(f.read())
            base64_string = base64_bytes.decode('utf-8')
        data = {
            "audio": base64_string,
            "audio_format": "wav",
            "sample_rate": 16000,
            "lang": 'zh_cn',
            "punc": True
        }
        res = requests.post(url=self.asr_url, data=json.dumps(data))
        if not res.json()['success']:
            raise HTTPError()
        text = res.json()['result']['transcription']
        if isinstance(text, str) and len(text) > 0:
            data = {
                "text": text
            }
            res = requests.post(url=self.text_url, data=json.dumps(data))
            return res.json()["result"]["punc_text"]
        return ""
