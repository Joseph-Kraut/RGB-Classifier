import pandas as pd
import sys

def distance(x,y):
    sum_distances = 0
    for i in range(len(x)):
        sum_distances += (x[i] - y[i]) ** 2
    return sum_distances ** 0.5

def split_data(data, ratio):
    #ratio is a decimal value that is the proportion that training data should make up
    number_data_points_training = int(ratio * len(data))
    #points were generated at random so we don't have to sample randomly from data
    training_data = data[:number_data_points_training]
    testing_data = data[number_data_points_training:]
    return (training_data, testing_data)

def find_most_common(list):
    #will return the most common element from a dictionary of counts for each class
    #Example input: a = {'blue': 1, 'green': 2, 'yellow': 0, 'red': 10, 'purple': 1} -> 'red'
    counts_dict = {}

    #constuct a dictionary of counts
    for i in range(len(list)):
        if list[i] not in counts_dict:
            counts_dict[list[i]] = 1
        else:
            counts_dict[list[i]] += 1

    return max(counts_dict, key=lambda x: counts_dict[x])


def classify_KNN(point, training_data, k):
    #apply the distance function to each point in training data
    distances = []

    for i in range(training_data.shape[0]):
        distances += [distance(point, list(training_data.loc[i])[:3])]

    training_data.loc[:, 'distance'] = distances
    training_data = training_data.sort_values('distance')
    return find_most_common(training_data[:k].label.tolist())

def parse_data_point(string):
    """(1,2,3)"""
    red = int(string[1])
    green = int(string[3])
    blue = int(string[5])
    return (red, green, blue)

def test(test_data, training_data, k):
    #the length of the test_data
    length = test_data.shape[0]
    results = 0 #this will be a sum of the positive results we will divide it by length later
    for i in range(length):
        rgb_values = list(test_data.loc[i])[:3]
        classification = classify_KNN(rgb_values, training_data, k)
        if classification.upper() == test_data.loc[i].label:
            results += 1

    return results / length

def main():
    #first step is to load the data
    #try catch loop for catching an empty data file
    raw_data = pd.read_csv("data.csv")
    #reorganize the columns
    raw_data = raw_data[['red', 'green', 'blue', 'label']]
    #we want to split the data into trianing and testing
    ratio = float(input("What ratio of training data do you want (0 to 1): "))
    training_data, testing_data = split_data(raw_data, ratio)

    #reset the indexing so we can index into the data from 0
    training_data = training_data.reset_index(drop=True)
    testing_data = testing_data.reset_index(drop=True)
    #choose between classifying a new point or testing on the testing_data
    choice = input("Do you want to classify, test, or done: ").upper()
    if choice == "CLASSIFY":
        input_point = parse_data_point(input("Enter a data point in form (r,g,b): "))
        print(classify_KNN(input_point, training_data, 5))
        main()
    elif choice == "TEST":
        number_neighbors = int(input("What should k be: "))
        print(test(testing_data, training_data, number_neighbors))
        main()
    elif choice == "DONE":
        print("Great!")
    else:
        print("Sorry not a valid input")
        main()

if __name__ == "__main__":
    main()
