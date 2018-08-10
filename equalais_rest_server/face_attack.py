import numpy as np
import keras
import tensorflow as tf
import keras as K

from cleverhans.attacks import FastGradientMethod
from cleverhans.utils_keras import cnn_model
from cleverhans.utils_keras import KerasModelWrapper


saved_model_name = "./model_2/model.ckpt"

# desired_image_size = (250, 250)
desired_image_size = (300, 300)
num_classes = 2

sess = tf.Session()

keras.backend.set_session(sess)

keras.layers.core.K.set_learning_phase(0)

# Define input TF placeholder
x = tf.placeholder(tf.float32, shape=(None, desired_image_size[0], desired_image_size[1], 3))

# model = cnn_model(img_rows=desired_image_size[0],
#                   img_cols=desired_image_size[1],
#                   channels=3,
#                   nb_filters=64,
#                   nb_classes=num_classes)

channels = 3
nb_filters = 64
model = K.Sequential()
model.add(K.layers.Convolution2D(nb_filters, (8, 8), strides=(2, 2),
                                 padding="same", activation='relu',
                                 input_shape=(desired_image_size[0],
                                              desired_image_size[1], channels)))
model.add(K.layers.Convolution2D(nb_filters * 2, (6, 6), strides=(2, 2),
                                 padding="valid", activation='relu'))
model.add(K.layers.Convolution2D(nb_filters * 2, (3, 3), strides=(2, 2),
                                 padding="valid", activation='relu'))
model.add(K.layers.Convolution2D(nb_filters * 4, (3, 3), strides=(2, 2),
                                 padding="valid", activation='relu'))
model.add(K.layers.MaxPooling2D(pool_size=(2, 2)))
model.add(K.layers.Flatten())
model.add(K.layers.Dense(100))
model.add(K.layers.Dense(num_classes))
model.add(K.layers.Activation('softmax'))


preds = model(x)

if keras.backend.image_dim_ordering() != 'tf':
    keras.backend.set_image_dim_ordering('tf')
    print("INFO: '~/.keras/keras.json' sets 'image_dim_ordering' to "
          "'th', temporarily setting to 'tf'")

saver = tf.train.Saver()
saver.restore(sess, saved_model_name)

wrap = KerasModelWrapper(model)
fgsm = FastGradientMethod(wrap, sess=sess)
adv_x = fgsm.generate(x, eps=0.1, clip_min=0.0, clip_max=1.0)
adv_x = tf.stop_gradient(adv_x)


def perturb(imgs):
    imgs = np.asarray(imgs)
    assert len(imgs.shape) == 4
    assert imgs.shape[1] == imgs.shape[2] == 300
    # assert imgs.shape[1] == imgs.shape[2] == 250
    assert imgs.shape[3] == 3
    assert (0.0 <= imgs).all() and (imgs <= 1.0).all()
    return sess.run(adv_x, feed_dict={x: imgs})




