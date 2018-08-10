NV_GPU=$1 nvidia-docker run -it --rm -p 6888:7888 -v $PWD/:/adversarial_attack socraticdatum/adversarial_attack:latest /bin/bash
