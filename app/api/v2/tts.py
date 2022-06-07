from flask import jsonify, request, current_app
from common.minio import upload_file
from . import v2_bp
from tts import TTSClient


client = TTSClient()
@v2_bp.route('/tts', methods=['POST'])
def tts():
    content = request.json
    text = content['text']
    if not text:
        return jsonify({
            "msg": "text 参数不存在",
            "code": 1
        })
    wav_file = client(text)
    current_app.logger.info('Wave file has been generated: {}'.format(wav_file))

    url = upload_file(wav_file)
    current_app.logger.info('Remove wave file: {}'.format(wav_file))
    return jsonify({
        "url": url,
        "msg": "OK",
        "code": 0
    })
