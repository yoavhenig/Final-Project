import time
from selenium import webdriver
from browsermobproxy import Server
from selenium.webdriver.chrome.options import Options
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
    ####'''''''''''''''''''''''''####
    # This code open proxy server with our arguments and open Chrome browser with those arguments.
    # The proxy help us to create HAR file with the name "try_har.json"
    # finally print the total time of GET request
    ####'''''''''''''''''''''''''#####
    # TODO: add for loop, generate indicative names to the files, create configuration file
    # remember to turn on/off the QUIC flag!

    server = Server(r"C:\Users\main_user\PycharmProjects\untitled2\FinalProject\browsermob-proxy-2.1.4\bin\browsermob-proxy")
    server.start()
    proxy = server.create_proxy()

    # # incognito window
    # chrome_options = webdriver.ChromeOptions()
    # proxy2 = proxy.proxy
    # chrome_options.add_argument("--incognito")
    # chrome_options.add_argument("-enable-quic")
    # chrome_options.add_argument('--proxy-server=%s' % proxy2)

    if not os.path.exists('youtube_results'):
        print("creating directory")
        os.makedirs('youtube_results')

    for x in range(0, RUN_TIME):
        options = webdriver.ChromeOptions()
        options.add_argument("user-data-dir=C:\\Users\\main_user\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
        options.add_argument("--incognito")
        options.add_argument("-enable-quic")
        driver = webdriver.Chrome(executable_path=r"C:\Users\main_user\Desktop\chromedriver_win32\chromedriver.exe", options=options)
        proxy.new_har("har_youtube{}".format(str(x)))
        start_time = time.time()
        driver.get("http://www.youtube.com/")
        end_time = time.time()
        total_time = end_time - start_time
        print("total time: {}".format(total_time))
        har_res = proxy.har

        data_folder = os.path.join("youtube_results")
        file_to_open = os.path.join(data_folder, '{}_youtube.har'.format((str(x))))
        with open(file_to_open, 'w+') as har_file:
            # har_file.write("our_total_time: "+str(total_time))
            json.dump(har_res, har_file)
        driver.close()
    server.stop()
    driver.quit()
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
