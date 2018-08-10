:'This script downloads the raw "Labeled Faces in the Wild" dataset

Dataset description:
13233 images
5749 people
1680 people with two or more images
250x250 pixel images
'

# Run this script for the root of this repository.
if [ ! -d ./raw_data/ ]; then
  # If raw_data directory doesn't exist create it
  mkdir ./raw_data/
fi

wget http://vis-www.cs.umass.edu/lfw/lfw.tgz --directory-prefix ./raw_data/
tar -xvzf ./raw_data/lfw.tgz --directory ./raw_data/
rm ./raw_data/lfw.tgz