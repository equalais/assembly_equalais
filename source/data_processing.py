from pathlib import Path
import numpy as np
from PIL import Image as pil_image


def import_images_from_directories(root_path, class_labels=None, resize_shape=(250, 250), max_images_per_class=None):
    root_path = Path(root_path)

    if class_labels is None or len(class_labels) == 0:
        class_labels = [c.name for c in list(root_path.iterdir())]

    if max_images_per_class is None:
        max_images_per_class = -1

    data = {}
    for class_path in root_path.iterdir():
        class_label = class_path.name
        if class_label in class_labels:
            class_images = []
            for image_path in sorted(list(class_path.iterdir()))[:max_images_per_class]:
                try:
                    img = pil_image.open(image_path.as_posix()).convert('RGB').resize(resize_shape)
                    class_images.append(np.asarray(img))
                except OSError:
                    print('Unable to open file {}, skipping...'.format(image_path))

            data[class_label] = np.asarray(class_images)

    assert len(data) == len(class_labels)
    class_labels = sorted(class_labels)

    X, Y, labels = None, None, {}
    for i, c in enumerate(class_labels):
        X = np.append(X, data[c], axis=0) if X is not None else data[c]
        y_c = np.zeros((data[c].shape[0], len(class_labels)), dtype=np.uint8)
        y_c[:, i] = 1
        Y = np.append(Y, y_c, axis=0) if Y is not None else y_c
        labels[i] = c

    print("The labels are: {}".format(labels))

    return X / 255.0, Y


if __name__ == "__main__":
    X, Y = import_images_from_directories('../data/cifar-10', class_labels=['airplane', 'automobile'], max_images_per_class=100)
    print(1)
