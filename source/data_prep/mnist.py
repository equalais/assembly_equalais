from pathlib import Path
from .utils import split_into_train_test


mnist_raw_data_path = Path('../datasets/raw/mnist')
prepared_data_path = Path('../datasets/prepared')


if __name__ == "__main__":
    prepared_path = split_into_train_test(mnist_raw_data_path,
                                          prepared_data_path,
                                          test_split_frac=0.1)