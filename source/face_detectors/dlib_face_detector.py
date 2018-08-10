import numpy as np
import dlib
from .face_detector import FaceDetector


class DlibFaceDetector(FaceDetector):

    def __init__(self):
        self._detector = dlib.get_frontal_face_detector()

    def _detect_face(self, img):
        return len(self._detector(np.asarray(img * 255.0, dtype=np.uint8), 1)) > 0
