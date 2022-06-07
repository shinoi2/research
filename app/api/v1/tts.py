from flask import send_file, request, current_app
from . import v1_bp
from tts import TTSClient

client = TTSClient()
@v1_bp.route('/tts', methods=['POST'])
def tts():
    content = request.json
    text = content['text']
    if not text:
        return "Text not found", 400
    wav_file = client(text)
    current_app.logger.info('Wave file has been generated: {}'.format(wav_file))

    return send_file(wav_file)
