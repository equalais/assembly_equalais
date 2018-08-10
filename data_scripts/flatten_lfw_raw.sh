# Move every file in each sub-directory of /lfw/ to /lfw/ and remove the sub-directory.

for D in ./raw_data/lfw/*; do mv $D/* ./raw_data/lfw/; rm -rf $D; done