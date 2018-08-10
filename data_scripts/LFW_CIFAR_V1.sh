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
echo -e "\n Executing lfw_crop_scale.py"
echo -e "\n *~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*"
python ./data_scripts/lfw_crop_scale.py

echo -e "\n *~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*"
echo -e "\n Executing download_cifar-10.sh"
echo -e "\n *~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*"
. ./data_scripts/download_cifar-10.sh

echo -e "\n *~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*"
echo -e "\n Executing unpickle_cifar-10.py"
echo -e "\n *~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*"
python ./data_scripts/unpickle_cifar-10.py

echo -e "\n *~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*"
echo -e "\n Executing make_cifar-11.py"
echo -e "\n *~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*"
python ./data_scripts/make_cifar-11.py

echo -e "\n *~*~*~*~*~*~*~*~*~*"
echo -e "\n Cleaning up ./data"
echo -e "\n *~*~*~*~*~*~*~*~*~*"
rm -rf ./data/cifar-10-batches-py
rm -rf ./data/lfw
