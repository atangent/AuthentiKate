from io_functions import read_data

def average(lst):
    'Generic average'
    return sum(lst)/len(lst)

def train():
    'Train a classifier and returns it'
    data = read_data('training.txt')
    zero = []
    one = []
    # creating subsets
    for element in data:
        if int(element[-1]) == 1: zero.append(element)
        else: one.append(element)

    clf = []
    for i in range(4):
        z = average([float(n[i]) for n in zero])
        o = average([float(n[i]) for n in one])
        clf.append(average([z, o]))

    return clf
