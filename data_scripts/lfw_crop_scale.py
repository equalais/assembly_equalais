#! /usr/bin/python

'''
Simple image pre-processing for Labeled Faces in the Wild.

In the current iteration, we're doing the following:
1. Crop the border to naively remove black space.
2. Scale the image down to a target size (e.g., 32x32 CIFAR-10 size) that
   will match the size of images with other labels.

We're starting off with CIFAR-10 because it has 10 classes each with
10000 images. This will let us create a balanced dataset of face
examples and non-examples. We will drop face observations to get to 10000.
'''


import numpy as np
import cv2
import os
import shutil



# Script options
# --------------

crop_image = True
scale_image = False



# Load haar cascade for face detection
# ------------------------------------

face_cascade_name = './utils/haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier()
face_cascade.load(face_cascade_name)



# -------------------------------
# Iterate through image directory
# -------------------------------

root_read = './data/lfw/'
root_write = './data/lfw_cropped_scaled/'

# If root_write directory exists overwrite it.
if os.path.exists(root_write):
    shutil.rmtree(root_write)
os.makedirs(root_write)

for filename in os.listdir(root_read):


    # Load image
    # ----------

    image = cv2.imread(os.path.join(root_read,filename))
    #image = cv2.cvtColor(image,0)
    #image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) #RGB


    # Crop
    # ----
    # Note: Cropping being done to naively remove black borders

    if crop_image:
        # Assuming image is divisble by 10!
        crop_length = 60
        #target_size = image.shape[0] - crop_length
        x0 = int((crop_length)/2)
        y0 = int((crop_length)/2)
        x1 = -x0
        y1 = -y0
        cr_image = image[x0:x1, y0:y1]
    else:
        cr_image = image


    # Scale
    # -----

    if scale_image:
        cifar_10_size = 32
        scale_size = cifar_10_size
        sm_image = cv2.resize(cr_image, (scale_size,scale_size))
    else:
        sm_image = cr_image


    # Save image
    # ----------

    write_path = os.path.join(root_write,filename)
    cv2.imwrite(write_path,sm_image)
    #rint(write_path)

print("lfw_cropped_scaled built")
