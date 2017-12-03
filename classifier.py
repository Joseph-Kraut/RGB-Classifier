import json

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

def classify_KNN(point, training_data, k):
    

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



if __name__ == "__main__":
    main()
