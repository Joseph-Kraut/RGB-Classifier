"""
    Allows a user to classify colors as labeled data, will rewrite data.csv to store this
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random
import pandas as pd

def generate_random_rgb():
    """Returns a tuple of three RGB values on range [0,1]"""
    return (random.uniform(0,1), random.uniform(0,1), random.uniform(0,1))

def convert_to_rgb(input):
    """Converts an RGB value on [0,1] to a more common [0, 255]"""
    return (int(input[0] * 255), int(input[1] * 255), int(input[2] * 255))

def main():
    data = []
    red, green, blue, label = [], [], [], []
    counter = 0
    #we want to start a loop that puts up a rect of a random rgb and then asks user for class
    while True:
        rgb = generate_random_rgb()
        fig = plt.figure()
        ax = fig.add_subplot(111, aspect='equal')
        ax.add_patch(
            patches.Rectangle((0,0), 1, 1, color=rgb)
        )
        plt.show(block=False)
        answer = input('Color (' + str(counter) + "): ").upper()

        if answer == "DONE":
            break
        else:
            label += [answer]
            converted = convert_to_rgb(rgb)
            red += [converted[0]]
            green += [converted[1]]
            blue += [converted[2]]
        plt.close()
        count += 1

    data = {'red': red, 'green': green, 'blue': blue, 'label': label}
    df = pd.DataFrame(data=data)
    df.to_csv('data.csv', index=False)
    print('Done!')


if __name__ == '__main__':
    main()
