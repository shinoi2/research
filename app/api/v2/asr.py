from urllib.error import HTTPError
from flask import jsonify, request, current_app
from common import get_audio
from . import v2_bp
from asr import ASRClient

client = ASRClient()
@v2_bp.route('/asr', methods=['POST'])
def asr():
    audio = get_audio()
    if audio is None:
        return jsonify({
            "msg": "audio 或 url 参数不存在",
            "code": 1
        })
    try:
        text = client(audio)
    except FileNotFoundError:
        return jsonify({
            "msg": "audio 或 url 文件非法",
            "code": 1
        })
    except Exception:
        return jsonify({
            "msg": "语音识别失败",
            "code": 1
        })
    return jsonify({
        "text": text,
        "msg": "OK",
        "code": 0
    })
