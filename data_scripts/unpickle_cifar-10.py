#! /usr/bin/python
'''
Unpickle CIFAR-10:

1. Write a directory for each unique label
2. Iterate through the data batches doing each of below
3. Grab dict.data, dict.filenames, dict.labels
4. For every image in a batch save each file to it's respective directory
'''

import os
import numpy as np
import shutil
import matplotlib.pyplot as plt


def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict

root_write = './raw_data/cifar-10'
root_batch = './raw_data/cifar-10-batches-py/'

label_set = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
label_dict = {
    0:'airplane',
    1:'automobile',
    2:'bird',
    3:'cat',
    4:'deer',
    5:'dog',
    6:'frog',
    7:'horse',
    8:'ship',
    9:'truck'
}

if os.path.exists(root_write):
    shutil.rmtree(root_write)
os.makedirs(root_write)

for label in label_set:
    label_dir = write_path = os.path.join(root_write,label_dict[label])
    os.makedirs(label_dir)

batch_list = ['data_batch_1', 'data_batch_2', 'data_batch_3', 'data_batch_4', 'data_batch_5', 'test_batch']

for batch in batch_list:

    print(batch)

    file = os.path.join(root_batch,batch)
    batch_dict = unpickle(file)
    filenames = batch_dict[b'filenames']
    filenames = [file.decode('ascii') for file in filenames]
    labels = batch_dict[b'labels']
    data = batch_dict[b'data']

    for idx in range(0,data.shape[0]):

        filename = filenames[idx]
        label = label_dict[labels[idx]]
        img = data[idx]
        img = np.transpose(np.reshape(img,(3, 32,32)), (1,2,0))

        write_path = os.path.join(root_write,label,filename)
        plt.imsave(write_path,img)
