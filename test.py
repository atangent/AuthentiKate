from io_functions import read_data
from train import train, average

def cmpr(l1, l2):
    'Compare two lists in the way described by assignment'
    lst = []
    for i in range(len(l1)):
        if float(l1[i]) >= float(l2[i]): lst.append(0)
        else: lst.append(1)
    return average(lst)

def rd(flt):
    'round the magic way'
    if flt != 0.5: return round(flt)
    else: return 1

def test(test, clf):
    'Test the classifier, display accuracy'
    data = read_data(test)
    pred = [1 if int(element[-1]) == int(rd(cmpr(element[:-1], clf))) else 0 for element in data]
    return float(pred.count(1)/len(pred)*100)
