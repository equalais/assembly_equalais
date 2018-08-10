:'This downloads the Python version of CIFAR-10.
'

# Run this script for the root of this repository.
if [ ! -d ./raw_data/ ]; then
  # If raw_data directory doesn't exist create it
  mkdir ./raw_data/
fi

wget https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz --directory-prefix ./raw_data/
tar -xvzf ./raw_data/cifar-10-python.tar.gz --directory ./raw_data/
rm ./raw_data/cifar-10-python.tar.gz
#mv ./raw_data/cifar-10-python ./raw_data/cifar-10
