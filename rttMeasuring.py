import time
from selenium import webdriver

driver = webdriver.Chrome("C:/Users/levid/OneDrive/Documents/year3/Final Project/chromedriver.exe")
rttArray = []
average = 0

for i in range(0, 100):
    startTime = time.time()
    driver.get("https://youtube.com")
    endTime = time.time()
    downloadTime = endTime - startTime
    rttArray.append(downloadTime)
    average += downloadTime


driver.quit()
print("Test completed in: %s seconds." % (average/100))


'''
how many requests, files (different sizes), packages size, dumminet(windows monitor), package loss, pickup measurement
'''