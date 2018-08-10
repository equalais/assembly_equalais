FROM nvidia/cuda:8.0-cudnn7-runtime-ubuntu16.04
FROM tensorflow/tensorflow:1.4.0-gpu-py3

RUN pip install --upgrade pip

RUN apt-get update && apt-get install git-all -y \
    wget \
	python3-tk
	
RUN pip install -qq -e git+http://github.com/tensorflow/cleverhans.git#egg=cleverhans

RUN pip --no-cache-dir install --upgrade ipython && \
	pip --no-cache-dir install \
        keras \
        opencv-python

WORKDIR /adversarial_attack
