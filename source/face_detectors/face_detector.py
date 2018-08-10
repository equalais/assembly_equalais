import numpy as np


class FaceDetector(object):

    def contains_a_face(self, img_or_img_array):
        assert len(img_or_img_array.shape) in [3, 4]
        assert (0.0 <= img_or_img_array).all() and (img_or_img_array <= 1.0).all()

        if len(img_or_img_array.shape) == 4:
            detections = []
            for i in range(img_or_img_array.shape[0]):
                detections.append(self._detect_face(img_or_img_array[i]))
            return np.asarray(detections, dtype=np.uint8)

        if len(img_or_img_array.shape) == 3:
            return self._detect_face(img_or_img_array)

    def _detect_face(self, img):
        raise NotImplementedError