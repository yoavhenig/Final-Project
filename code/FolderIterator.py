import os
import glob
import csv
import numpy as np
import matplotlib.pyplot as plt


def getResult(file):
    with open(file, "r", encoding="utf-8", errors="ignore")as f:
        fileToGraph = csv.reader(f)
        data = [row for row in fileToGraph]
        row_count = len(data)  # represent the amount of rows in the csv file
        totalRequest = 0
        totalTime = 0
        totalWeight = 0
        for i in range(1, row_count-1):
            totalRequest += float(data[i][1])
            totalTime += float(data[i][2])
            totalWeight += float(data[i][3])
        requests = totalRequest / (row_count - 2)
        weight = totalWeight / (row_count - 2)
        time = totalTime / (row_count - 2)
    return [requests, time, weight]


def plot_results_to_bar_charts(filename, requests, time, weight):
    # REQUESTS plotting:
    y_pos = np.arange(len(filename))
    plt.bar(y_pos, requests, align='center', alpha=0.5, color=['red', 'blue', 'yellow', 'black'])
    plt.xticks(y_pos, filename)
    plt.title('Requests:')
    plt.show()

    # TIME plotting:
    y_pos = np.arange(len(filename))
    plt.bar(y_pos, time, align='center', alpha=0.5, color=['red', 'blue', 'yellow', 'black'])
    plt.xticks(y_pos, filename)
    plt.title('Time:')
    plt.show()

    # WEIGHT plotting:
    y_pos = np.arange(len(filename))
    plt.bar(y_pos, weight, align='center', alpha=0.5, color=['red', 'blue', 'yellow', 'black'])
    plt.xticks(y_pos, filename)
    plt.title('Weight:')
    plt.show()

def main():
    filename = []; requests = []; time = []; weight = []
    for file in glob.glob('*.csv'):
        filename.append(os.fsdecode(file))
        # Get results from each file:
        file_result = getResult(file)

        # make arrays for every parameter:
        requests.append(file_result[0])
        time.append(file_result[1])
        weight.append(file_result[2])
    # print(filename)
    plot_results_to_bar_charts(filename, requests, time, weight)

if __name__ == "__main__":
    main()
