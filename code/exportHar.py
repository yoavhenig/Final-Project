import time
from selenium import webdriver
from browsermobproxy import Server
import json
"""
in order to compile this program the browsermobproxy server file should be in the python project
'''''''''''''''''''''''''''
This code open proxy server with our arguments and open Crhome browser with those arguments.
The proxy help us to create HAR file with the name "try_har.json"
finally print the total time of GET request
'''''''''''''''''''''''''''
"""

# TODO: add for loop, generate indicative names to the files, create configuration file
# remember to turn on/off the QUIC flag!


server = Server(r"C:\Users\main_user\PycharmProjects\untitled2\FinalProject\browsermob-proxy-2.1.4\bin\browsermob-proxy")
server.start()
proxy = server.create_proxy()

# incognito window
chrome_options = webdriver.ChromeOptions()
proxy2 = proxy.proxy
chrome_options.add_argument("--incognito")
chrome_options.add_argument("-disable-quic")
chrome_options.add_argument('--proxy-server=%s' % proxy2)

driver = webdriver.Chrome(
    r"C:\Users\main_user\Desktop\chromedriver_win32\chromedriver.exe"
                          ,chrome_options=chrome_options)

proxy.new_har("try_har")
start_time = time.time()
driver.get("http://www.youtube.com/")
end_time = time.time()
rtt_time = end_time - start_time
har_res = proxy.har
with open ('try_har.json','w') as har_file:
    json.dump(har_res, har_file)

server.stop()
driver.quit()
print("so far %s" % rtt_time)