import numpy as np
import logging
from datetime import datetime
from flask import Flask, request, send_file, Response
from werkzeug.utils import secure_filename
import json
import io
import base64
from PIL import Image as pil_image
from flask_cors import CORS
import face_attack


ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg']


app = Flask(__name__)
CORS(app)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST', 'PUT'])
def face():
    request_time = datetime.now()
    if request.method != 'POST':
        return json.dumps({'error': "This endpoint only supports POST requests."})

    if len(request.files) == 0:
        return json.dumps({'error': "The 'files' payload was empty."})

    if request.files.get('image') is None:
        return json.dumps({'error': "The 'files' payload did not contain an 'image' key (but did find keys: {}).".format(', '.join(request.files.keys()))})

    image = request.files.get('image')
    filename = secure_filename(image.filename)

    if not allowed_file(filename):
        return json.dumps({'error': "The /diagnose endpoint only supports image types: {}"
                          .format(', '.join(ALLOWED_EXTENSIONS))})

    image_bytes = image.read()
    response_obj = {
        'elapsed_time_seconds': (datetime.now() - request_time).total_seconds(),
        'response_image': image_bytes
    }
    # print(response_obj)
    img = pil_image.open(io.BytesIO(image_bytes)).convert('RGB')
    orig_size = img.size
    # img = img.resize((250, 250))
    img = img.resize((300, 300))
    img = np.asarray(img) / 255.0
    attacked_img = face_attack.perturb([img])[0]
    attacked_img_buff = io.BytesIO()
    pil_image.fromarray(np.uint8(attacked_img*255)).resize(orig_size).save(attacked_img_buff, 'PNG')
    # return send_file(io.BytesIO(attacked_img_buff.getvalue()),
    #                  attachment_filename='equal-ias_' + filename,
    #                  mimetype='image/PNG')
    return send_file(io.BytesIO(base64.b64encode(attacked_img_buff.getvalue())),
                     as_attachment=True,
                     attachment_filename='equal-ias_' + filename,
                     mimetype='image/PNG;base64'
                     )


# @app.route('/')
# @app.route('/readiness_check')
# @app.route('/liveness_check')
# @app.route('/_ah/health')
# def check():
#     return Response('OK', status=200)


@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
