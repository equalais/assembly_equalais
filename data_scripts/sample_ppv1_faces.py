#! /usr/bin/python

import os
import shutil
import random

# Randomly select subtraction batch from faces to reduce to n=6000
random.seed(12345)
face_src = './data/private_proof_v1/face'

files = sorted(os.listdir(face_src))
file_count = len(files)

holdout_size = file_count - 6000
random_files_idx = random.sample(range(0, file_count), holdout_size)
random_files_names = [files[idx] for idx in random_files_idx]

# Create cifar-11_face_holdout
root_holdout = './data/private_proof_v1/face_holdout/'

# If root_write directory exists overwrite it.
if os.path.exists(root_holdout):
    shutil.rmtree(root_holdout)
os.makedirs(root_holdout)

# Move subtraction batch to cifar-11_face_holdout
for filename in random_files_names:
    src = os.path.join(face_src,filename)
    shutil.move(src,root_holdout)