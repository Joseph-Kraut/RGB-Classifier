import json
import sys

def distance(x,y):
    sum_distances = 0
    for i in range(len(x)):
        sum_distances += (x[i] - y[i]) ** 2
    return sum_distances ** 0.5

def split_data(data, ratio):
    #ratio is a decimal value that is the proportion that training data should make up
    number_data_points_training = int(ration * len(data))
    #points were generated at random so we don't have to sample randomly from data
    training_data = data[:number_data_points_training]
    testing_data = data[number_data_points_training:]
    return (training_data, testing_data)

def find_most_common(counts_dict):
    #will return the most common element from a dictionary of counts for each class
    #Example input: a = {'blue': 1, 'green': 2, 'yellow': 0, 'red': 10, 'purple': 1} -> 'red'
    return max(counts_dict, key=lambda x: a[x])


def classify_KNN(point, training_data, k):

    #add the distances to each element of the training_data

    #creates a list of size k of all max ints
    k_closest = [sys.maxsize] * k

    for i in range(len(training_data)):
        #calculate the distance for the point
        data_point = training_data[i][1]
        dist = distance(point, data_point)

    #sort the element with key being distance
    training_data = sorted(training_data, key=lambda x: x[2])
    classification = find_most_common([x[0] for x in training_data][:k])
    return classification

def parse_data_point(string):
    """(1,2,3)"""
    red = int(string[1])
    green = int(string[3])
    blue = int(string[5])
    return (red, green, blue)

def test(test_data, training_data, k):
    results = 0 #this will be a sum of the positive results we will divide it by length later
    for i in range(len(test_data)):
        classification = classify_KNN(test_data[i][1], training_data, k)
        if classification.upper() == test_data[i][0]:
            results += 1

    return results / len(test_data)

def main():
    #first step is to load the data
    #try catch loop for catching an empty data file
    try:
        input_file = open('data.txt', 'r')
        json_string = input_file.read()
        raw_data = json.loads(json_string)
    except json.decoder.JSONDecodeError as err:
        raw_data = [[]]
        print('no data')

    #we want to split the data into trianing and testing
    ratio = int(input("What ratio of training data do you want (0 to 1): "))
    training_data, testing_data = split_data(raw_data, ratio)
    #choose between classifying a new point or testing on the testing_data
    choice = input("Do you want to classify, test, or done: ").upper()
    if choice == "CLASSIFY":
        input_point = parse_data_point(input("Enter a data point in form (r,g,b): "))
        print(classify_KNN(input_point, training_data, 5))
        main()
    elif choice == "TEST":
        number_neighbors = int(input("What should k be: "))
        print(test(testing_data, training_data, number_neighbors))
    elif choice == "DONE":
        print("Great!")
    else:
        print("Sorry not a valid input")
        main()

if __name__ == "__main__":
    main()
