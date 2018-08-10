#!/bin/bash

echo -e "\n *~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*"
echo -e "\n Launching script."
echo -e "\n *~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*"
echo -e "\n Executing download_lfw_raw.sh"
. ./data_scripts/download_lfw_raw.sh

echo -e "\n *~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*"
echo -e "\n Executing flatten_lfw_raw.sh"
echo -e "\n *~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*"
. ./data_scripts/flatten_lfw_raw.sh

echo -e "\n *~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*"
echo -e "\n Executing download_cifar-10.sh"
echo -e "\n *~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*"
. ./data_scripts/download_cifar-10.sh

echo -e "\n *~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*"
echo -e "\n Executing unpickle_cifar-10.py"
echo -e "\n *~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*"
python ./data_scripts/unpickle_cifar-10.py

echo -e "\n *~*~*~*~*~*~*~*~*~*"
echo -e "\n Cleaning up ./raw_data"
echo -e "\n *~*~*~*~*~*~*~*~*~*"
rm -rf ./raw_data/cifar-10-batches-py

echo -e "\n *~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*"
echo -e "\n Executing download_private_proof.py"
echo -e "\n *~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*"
python ./data_scripts/download_private_proof_v1.py

echo -e "\n *~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*"
echo -e "\n Pushing the data folder to gs://raw_data"
echo -e "\n *~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*"
python ./data_scripts/upload_raw_data_to_gc.py

echo -e "\n *~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*"
echo -e "\n Done! "
echo -e "\n *~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*"
