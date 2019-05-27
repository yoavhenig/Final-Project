import time
from selenium import webdriver

driver = webdriver.Chrome(r"C://Users//moriya&yoav//Desktop//chromedriver_win32//chromedriver.exe")
# driver.implicity_wait(10)
driver.maximize_window()

start_time = time.time()
driver.get("http://www.youtube.com/")

rtt_time = time.time()-start_time
driver.close()
driver.quit()

print("so far %s" % rtt_time)
