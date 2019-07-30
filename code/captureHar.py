import time
import json
import os
import subprocess
from haralyzer import HarParser
import csv

RUN_TIME = 2
CHROME_TYPE = "google-chrome --remote-debugging-port=9222"
# "google-chrome --remote-debugging-port=9222 -incognito" use this for incognito
# google-chrome --remote-debugging-port=9222 --headless (--incognito)


def har_analyzer(file, writer, folder):
    path = os.path.join(folder, file)
    with open(path, 'r', encoding='utf8') as f:
        har_parser = HarParser(json.loads(f.read()))
    requests = 0
    total_weight = 0
    max_time = 0
    min_time = 0

    for page in har_parser.pages:
        requests += page.entries.__len__()
        min_time = float(page.entries[0]['startedDateTime'][17:23]) * 1000
        for entry in page.entries:
            total_weight += entry['response']['content']['size']
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


def chrome_init():
    subprocess.Popen(CHROME_TYPE, stdout=subprocess.PIPE, shell=True)
    time.sleep(3)


def run_har_capture(harCap, folder):
    if not os.path.exists(folder):
        print("creating directory")
        os.makedirs(folder)

    website = " https://youtube.com"
    for i in range(0,RUN_TIME):
        file = "/res_{}.har".format(i)
        os.system(harCap+folder+file+website)
        print(harCap+file+website)
    print("finished successfully")


def scenario(file, har_cap, folder):
    summary = open(file, 'w', newline='')
    headers = ['Filename', 'Requests', 'Total Iime (Sec)', 'Total Weight (MB)']
    writer = csv.writer(summary)
    writer.writerow(headers)

    run_har_capture(har_cap, folder)
    for filename in os.listdir(folder):
        har_analyzer(filename, writer, folder)

    averageR = "=AVERAGE(B2:B" + str((RUN_TIME + 1)) + ")"
    averageT = "=AVERAGE(C2:C" + str((RUN_TIME + 1)) + ")"
    averageW = "=AVERAGE(D2:D" + str((RUN_TIME + 1)) + ")"
    averageRow = ['Average:', averageR, averageT, averageW]
    writer.writerow(averageRow)


# -------------------------------------******************------------------------------#


def main():
    filename_results = input("Choose filename for results\n")

    # open chrome browser
    chrome_init()

    # FIRST - regular
    filename_r = filename_results + ".csv"
    har_cap = "chrome-har-capturer -k -o "
    folder = filename_results
    scenario(filename_r, har_cap, folder)

    # SECOND - incognito
    filename_inco = filename_results + "_inco.csv"
    har_cap = "chrome-har-capturer -o "
    folder = filename_results + '_inco'
    scenario(filename_inco, har_cap, folder)


if __name__ == "__main__":
    main()
