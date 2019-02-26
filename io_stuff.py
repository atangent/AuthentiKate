"""
This module contains i/o operations
"""
from web_scraper import get_all_data
import urllib.request

def build_dataset(page='https://archive.ics.uci.edu/ml/machine-learning-databases/00267/data_banknote_authentication.txt'):
    'Get data from link, write to the local dir'
    stream = urllib.request.urlopen(page)
    data = get_all_data(stream, ',')
    trainfile = open('training.txt', 'w')
    testfile = open('testing.txt', 'w')
    counter = 0
    for line in data:
        if counter % 2 == 0:
            for element in line:
                trainfile.write(str(element) + ',')
            trainfile.write('\n')
        else:
            for element in line:
                testfile.write(str(element) + ',')
            testfile.write('\n')
        counter += 1

    trainfile.close()
    testfile.close()

def read_data(name):
    'Read data in the format that build_dataset creates'
    f = open(name, 'r')
    data = [x for x in [i.split(',')[:-1] for i in f.readlines()]]
    f.close()
    return data





