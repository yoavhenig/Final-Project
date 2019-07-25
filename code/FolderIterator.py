import os
import csv
from builtins import print
import numpy as np
import matplotlib.pyplot as plt

folderPath = os.path.dirname(os.path.abspath(__file__))+"\\"
# folderPath = "C:\\Users\\Ori\\Desktop\\chromedriver\\1\\"
scenarioName = []
totalScenarioRequest = []
totalScenarioTime = []
totalScenarioWeight = []
filesCounter = 0
directory = os.fsencode(folderPath)
for file in os.listdir(directory):
    filesCounter += 1
    filename = os.fsdecode(file)
    scenarioName.append(filename)
    if filename != "FolderIterator.py":
        fileToGraph = csv.reader(open(folderPath + filename))
        data = [row for row in fileToGraph]
        fileToGraph = csv.reader(open(folderPath + filename))
        row_count = sum(1 for row in fileToGraph)  # represent the amount of rows in the csv file
        totalRequest = 0
        totalTime = 0
        totalWeight = 0
        for i in range(1, (row_count - 1)):
            totalRequest += float(data[i][1])
            totalTime += float(data[i][2])
            totalWeight += float(data[i][3])
        totalRequest = totalRequest / (row_count - 2)
        totalWeight = totalWeight / (row_count - 2)
        totalTime = totalTime / (row_count - 2)
        totalScenarioRequest.append(totalRequest)
        totalScenarioTime.append(totalTime)
        totalScenarioWeight.append(totalWeight)

incomesReq = []
incomesTime = []
incomesWeight = []
nameOfGraph = ['Request', 'Time', 'Weight']
for x in range(1, 4):
    currentObjects = []
    print(x)
    for i in range(0, filesCounter-1):
        currentObjects.append(scenarioName[i])
        if x == 1:
            incomesReq.append(totalScenarioRequest[i])
        if x == 2:
            incomesTime.append(totalScenarioTime[i])
        if x == 3:
            incomesWeight.append(totalScenarioWeight[i])
    
    y_pos = np.arange(len(currentObjects))
    if x == 1:
        plt.bar(y_pos, incomesReq, align='center', color=['red', 'blue', 'yellow', 'black'])
    if x == 2:
        plt.bar(y_pos, incomesTime, align='center', color=['red', 'blue', 'yellow', 'black'])
    if x == 3:
        plt.bar(y_pos, incomesWeight, align='center', color=['red', 'blue', 'yellow', 'black'])
    plt.xticks(y_pos, currentObjects)
    plt.ylabel('scale')
    plt.xlabel('file name')
    plt.title(nameOfGraph[x-1])
    plt.show()

# print(filesCounter)
# print("total wight:" + str(totalScenarioWeight) +"\ntotal time:" + str(totalScenarioTime) + "\ntotal request:" + str(totalScenarioRequest))
# incomes = [totalScenarioRequest, totalScenarioTime, totalScenarioWeight]
# plt.bar(y_pos, incomes, align='center')
# plt.xticks(y_pos, objects)
# plt.ylabel('scale')
# plt.xlabel('data')
# plt.title('temp')
# plt.show()
