import json

def distance(x,y):
    sum_distances = 0
    for i in range(len(x)):
        sum_distances += (x[i] - y[i]) ** 2
    return sum_distances ** 0.5
