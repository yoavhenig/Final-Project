import time
import json
import os
from haralyzer import HarParser
import csv

RUN_TIME = 5


def har_analyzer(file, writer):
    path = os.path.join('youtube_results',file)
    with open(path, 'r', encoding='utf8') as f:
        har_parser = HarParser(json.loads(f.read()))
    requests = 0
    total_weight = 0

    for page in har_parser.pages:
        requests += page.entries.__len__()
        max_time = 0
        min_time = float(page.entries[0]['startedDateTime'][17:23]) * 1000
        for entry in page.entries:
            total_weight += entry['response']['bodySize']
            endTime = entry['time'] + float(entry['startedDateTime'][17:23]) * 1000
            if endTime > max_time:
                max_time = endTime

    total_weight = total_weight / 1000000
    total_time = (max_time - min_time) / 1000

    # print("Total time: {0}(seconds)".format(har_parser.har_data['pages'][0]['pageTimings']['onLoad']/1000))
    print("Total requests: ", requests)
    print("Total weight: {0}(MB)".format(total_weight))
    print("Total time: {0}(S)".format(total_time))
    writer.writerow([file, requests, total_time, total_weight])


def run_selenium():
    harCap = "chrome-har-capturer -o "
    data_folder = os.path.join("youtube_results")
    website = " https://youtube.com"
    for i in range(1,RUN_TIME):
        file = "/res_{}.har".format(i)
        os.system(harCap+data_folder+file+website)
    print("finished successfully")

# -------------------------------------******************------------------------------#


def main():
    filename_results = input("Choose filename for results\n")
    filenam_r = filename_results + ".csv"
    summary = open(filenam_r, 'w', newline='')
    headers = ['Filename', 'Requests', 'Total Iime (Sec)', 'Total Weight (MB)']
    writer = csv.writer(summary)
    writer.writerow(headers)

    run_selenium()
    for filename in os.listdir('youtube_results'):
        har_analyzer(filename, writer)

    averageR = "=AVERAGE(B2:B"+str((RUN_TIME+1))+")"
    averageT = "=AVERAGE(C2:C"+str((RUN_TIME+1))+")"
    averageW = "=AVERAGE(D2:D"+str((RUN_TIME+1))+")"
    averageRow = ['Average:', averageR, averageT, averageW]
    writer.writerow(averageRow)

if __name__ == "__main__":
    main()
