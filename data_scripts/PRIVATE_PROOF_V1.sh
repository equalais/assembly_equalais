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
echo -e "\n Executing download_private_proof.py"
echo -e "\n *~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*"
python ./data_scripts/download_private_proof_v1.py

echo -e "\n *~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*"
echo -e "\n Migrate faces to dataset directory"
echo -e "\n *~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*"
mv ./data/lfw/ ./data/face
mv ./data/face/ ./data/private_proof_v1

echo -e "\n *~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*"
echo -e "\n Sample faces, creating holdout set"
echo -e "\n *~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*"
python ./data_scripts/sample_ppv1_faces.py

echo -e "\n *~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*"
echo -e "\n Done! "
echo -e "\n *~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*"
