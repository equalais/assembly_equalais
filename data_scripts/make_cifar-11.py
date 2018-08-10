#! /usr/bin/python

import os
import shutil
import random


# Move lfw_cropped_scaled into cifar-10
root_lfw = "./data/lfw_cropped_scaled/"
dest_lfw = "./data/cifar-10/"

shutil.move(root_lfw,dest_lfw)


# Rename cifar-10 to cifar 11
os.rename('./data/cifar-10','./data/cifar-11')


# Rename lfw_cropped_scaled to faces
os.rename('./data/cifar-11/lfw_cropped_scaled/','./data/cifar-11/face')


# Randomly select subtraction batch from faces to reduce to n=6000
random.seed(12345)

files = sorted(os.listdir('./data/cifar-11/face'))
file_count = len(files)

holdout_size = file_count - 6000
random_files_idx = random.sample(range(0, file_count), holdout_size)
random_files_names = [files[idx] for idx in random_files_idx]

# Create cifar-11_face_holdout
root_holdout = './data/face_holdout/'

# If root_write directory exists overwrite it.
if os.path.exists(root_holdout):
    shutil.rmtree(root_holdout)
os.makedirs(root_holdout)

# Move subtraction batch to cifar-11_face_holdout
for filename in random_files_names:
    holdout_src = './data/cifar-11/face'
    src = os.path.join(holdout_src,filename)
    holdout_dst = './data/face_holdout/'
    shutil.move(src,holdout_dst)
