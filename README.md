# Assembly equalAIs

## Notebooks to help this all make sense

### Data prep

* [Haar Cascades face detector](https://github.com/equalais/assembly_equalais/blob/master/notebooks/sandbox/extract_faces_test.ipynb)
* [Haar Cascades face detector blur playground](https://github.com/equalais/assembly_equalais/blob/master/notebooks/sandbox/haar_cascades_blur.ipynb)
* [Make cifar](https://github.com/equalais/assembly_equalais/blob/master/notebooks/sandbox/make_cifar-11.ipynb)
* [Unpack cifar](https://github.com/equalais/assembly_equalais/blob/master/notebooks/sandbox/cifar-10_flatten.ipynb)
* [Image cropping and scaling playground](https://github.com/equalais/assembly_equalais/blob/master/notebooks/data_prep/image%20cropping%20playground.ipynb)

### Cleverhans introduction

* [Whitebox FGSM attack with and without adversarial training](https://github.com/equalais/assembly_equalais/blob/master/notebooks/cleverhans_boilerplate/mnist_whitebox_fgsm_plus_adversarial_training.ipynb)
* [Blackbox FGSM attack using a subsitution model trained with jacobian augmentation ](https://github.com/equalais/assembly_equalais/blob/master/notebooks/cleverhans_boilerplate/mnist_blackbox_substitution_fgsm.ipynb)

### Detector evaluation

* [Confusion matrix of the detectors over our dataset](https://github.com/equalais/assembly_equalais/blob/master/notebooks/evaluation/detector%20confusion%20matrix.ipynb)

## Environments

### Using Docker (recommended!)

To get started you may want to use the associated docker image. To do this you'll need [docker](https://docs.docker.com/engine/installation/linux/ubuntulinux/) and [nvidia-docker](https://github.com/NVIDIA/nvidia-docker/wiki/Why%20NVIDIA%20Docker) (for GPU use). If you've installed these you'll need to get the following image:

`docker pull socraticdatum/adversarial_attack:latest`

Alternatively, you could build the image from source using the Dockerfile provided in this repository.

Once you've cloned this repository, from the root of this repo run:
1. `. ./docker_scripts/launch_adversarial-docker.sh 0` to launch the docker container with nvidia docker your first GPU.
2. `. ./docker_scripts/launch_jupyter` to start a jupyter notebook.
    - This will pipe a jupyter notebook from the docker container on your server, being available at `<server-address>:6888`.

For more details see the bash scripts. If you add a data directory in the root of this directory it will be made available in the docker container since the root of this directory is mounted to the docker container.

#### The Docker image includes:
- Python 3.5
- Tensorflow, Keras
- Cleverhans
- OpenCV, Pillow
- Jupyter, Matplotlib, Sci-kit Learn

A built version of the docker image is available at:
https://hub.docker.com/r/socraticdatum/adversarial_attack/


### Using pipenv locally

1. You will need to first make sure you have the required `dlib` [dependencies](https://www.pyimagesearch.com/2017/03/27/how-to-install-dlib/)
1. Install/configurature [pipenv](https://docs.pipenv.org/)
1. In the top-level folder, run `pipenv install` to install all the required packages
1. To use Jupyter notebooks inside of a pipenv environment:
    1. First, configure Jupyter notebooks to use the pipenv environment, run: `pipenv run python -m ipykernel install
     --user --name="<environment-name>"`. The `<environment-name>` is typically found in `~/.virtualenvs` and will look something
like `assembly_melt-zSdd0Kve`.
    1. Then either start the pipenv shell (using `pipenv shell` and run `jupyter notebook` inside the shell) or
    just run `pipenv run jupyter notebook`
    1. When you start new notebooks, make sure you're using the `<environment-name>` kernel (this can always be
    changed in `Kernel -> Change Kernel`)

## Building Datasets

### Private Proof, Version 1

[Labeled Faces in the Wild](http://vis-www.cs.umass.edu/lfw/)
 - 13233 images of faces
 - 5749 people
 - 1680 people with two or more images
 - 250x250 resolution

 Manually pulled images from Google search. Classes:
 - Architecture
 - Insect
 - Bag
 - Machinery
 - Font
 - Landscape
 - Ring

Each of these classes have fewer than 1000 observations. Additionally, some of the images don't download properly (e.g., because they're not jpgs but are attempted to be downloaded as jpgs), so you'll need to filter these (e.g., try/exception loading).

The above classes were selected based on overall consistency in Google search and that they tended to have few people (with faces shown) as compared to search results for other potential classes.

To download a .zip of this dataset:
https://drive.google.com/file/d/11oOYf9ff6e-Mn9-jXNG7GZsqzV5l0dZZ/view?usp=sharing

To build this dataset execute the following script from the root of this repository:
`. ./data_scripts/PRIVATE_PROOF_V1.sh`

### CIFAR-11 (LFW+CIFAR), Version 1

[Labeled Faces in the Wild](http://vis-www.cs.umass.edu/lfw/)
 - 13233 images of faces
 - 5749 people
 - 1680 people with two or more images

[CIFAR-10](https://www.cs.toronto.edu/~kriz/cifar.html).
 - The CIFAR-10 dataset consists of 60000 32x32 colour images in 10 classes, with 6000 images per class.

To build this dataset execute the following script from the root of this repository.

`. ./data_scripts/LFW_CIFAR_V1.sh`

#### How we build the dataset

![LFW-cropping-scaling](https://github.com/equalais/assembly_equalais/blob/master/utils/LFW_crop_scale.jpg)

We construct the dataset by cropping the border of every LFW image to naively remove black borders. Then, we scale each image to 32x32 to match the dimensions of the CIFAR-10 images.

Finally, we combine the two datasets, added an 11th "face" category to CIFAR-10, creating CIFAR-11. We randomly sample a holdout set from the face category so that the face category will match the other categories by having 6000 observations. The holdout set is also provided in `./data`.
