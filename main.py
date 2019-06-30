# Import modules
from io_functions import build_dataset, read_data
from train import train
from test import test


def main():
    page = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00267/data_banknote_authentication.txt'
    build_dataset(page)
    clf = train()
    acc = test('testing.txt', clf)
    print("Test accuracy: %f%%" %acc)

    
# Test
if __name__ == '__main__':
    main()
