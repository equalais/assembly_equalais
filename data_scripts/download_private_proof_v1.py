#! /usr/bin/python

import requests
import os
import shutil
import cv2


overwrite_files = True

# Create list of our files that contain urls
read_path = './data_scripts/private_proof_v1/'
corpus_list = []
for root, dirs, files in os.walk(read_path):
    for file in files:
        corpus_list.append(file)

# You could add code to create ./data if ./data doesn't exist.
# Create private_proof_v1 directory
write_path = './raw_data/private_proof_v1'
if overwrite_files:
    if os.path.exists(write_path):
        shutil.rmtree(write_path)
os.makedirs(write_path)

for corpus in corpus_list:

    # Create list of image urls
    fname = os.path.join(read_path, corpus)
    with open(fname) as f:
        url_list = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    url_list = [x.strip() for x in url_list]

    # Create directory for the corpus
    general_label = corpus[:-4]
    corpus_path = os.path.join(write_path, general_label)
    if overwrite_files:
        if os.path.exists(corpus_path):
            shutil.rmtree(corpus_path)
    os.makedirs(corpus_path)

    print(len(url_list))
    print(corpus_path)

    # Download and save the images to disk
    for i, target_url in enumerate(url_list):
        try:
            r = requests.get(target_url)

        # Commonly privacy blocking
        except:
            continue

        print(target_url)
        extension = target_url.split('.')[-1].lower()
        if extension not in {'jpg', 'jpeg', 'png'}:
            continue
        filename = ''.join([general_label, '_', str(i), '.', extension])
        file_write_path = os.path.join(corpus_path, filename)
        f = open(file_write_path, "wb")
        f.write(r.content)
        f.close()

        # check if it is able to be loaded as a valid image file
        loaded_img = cv2.imread(file_write_path)
        if loaded_img is None:
            print("Removing file {}, it could not be loaded as a valid image!".format(file_write_path))
            os.remove(file_write_path)
        elif loaded_img.shape != (250, 250, 3):
            print("Removing file {}, it must've been some form of corrupted, it loaded as the incorrect shape!".format(file_write_path))
            os.remove(file_write_path)
        elif os.stat(file_write_path).st_size < 500:
            print("Removing file {}, it is too small to be a valid image (<0.5 kB)!".format(file_write_path))
            os.remove(file_write_path)
        elif os.stat(file_write_path).st_size > 75000:
            print("Removing file {}, it is too large to be a valid image (>75 kB)!".format(file_write_path))
            os.remove(file_write_path)
