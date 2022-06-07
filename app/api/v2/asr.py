from flask import jsonify, request, current_app
from common import get_audio
from . import v2_bp
from asr import ASRClient

client = ASRClient()
@v2_bp.route('/asr', methods=['POST'])
def asr():
    audio = get_audio()
    if not text:
        return jsonify({
            "msg": "audio 或 url 参数不存在",
            "code": 1
        })
    text = client(audio)
    return jsonify({
        "text": text,
        "msg": "OK",
        "code": 0
    })
