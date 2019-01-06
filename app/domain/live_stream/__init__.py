import cv2
import dlib
import base64
import numpy as np
from app import config
from appfly.app import app
from imutils import face_utils

predictor = dlib.shape_predictor(config['LANDMARKS68'])

def base64_to_cv2(uri):
    encoded_data = uri.split(',')[1]
    nparr = np.fromstring(base64.b64decode(app.images.get().split('base64')[-1]), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return img


# def get_face_points(shape):
#     return np.array([
#                     shape[33],     # Nose tip
#                     shape[8],      # Chin
#                     shape[36],     # Left eye left corner
#                     shape[45],     # Right eye right corne
#                     shape[48],     # Left Mouth corner
#                     shape[54]      # Right mouth corner
#                 ], dtype="double")

def _dog():
        """Returns a dog frame."""
        fh = open("/home/italojs/dev/python/api-flask-noalvo-demo/app/domain/live_stream/static/funny-dogs.jpg", "rb")
        frame = fh.read()
        fh.close()
        return frame

def gen_livestream():
    """Video streaming generator function."""

    flag = True
    frame = _dog()
    while True:
        time.sleep(0.02)
        if app.images.qsize():
            image = app.images.get()
            if flag:
                image = base64_to_cv2(image)
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                detector = dlib.get_frontal_face_detector()
                rects = detector(gray, 0)
                for (i, rect) in enumerate(rects):
                    shape = predictor(gray, rect)
                    shape = face_utils.shape_to_np(shape)
                
                    for (x, y) in shape:
                        cv2.circle(image, (x, y), 2, (0, 255, 0), -1)
                _, frame = cv2.imencode('.jpg', image)
        else:
            frame = _dog()
        # print(position)
        flag = not flag
        # yield ('Content-Type: image/jpeg\r\n\r\n' + base64.b64encode(frame).decode("utf-8") + '\r\n')

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

