# Final-Project
### Computer Science final project
##### Uriel Fluss, Levi Dworkin, Ori Moldovan, Yoav Henig
<br />
Measuring QUIC - google new protocol performance compare to known protocols (h2..).<br />
<br />
We use __selenium__ python library https://pypi.org/project/selenium/
    from selenium import webdriver
to open chrome and navigate through the internet and __browsermob-proxy__ python library https://pypi.org/project/browsermob-proxy/
    from browsermobproxy import Server
to export the sniffing data into HAR file.<br />
To analyze network traffic reported in the HAR file we use __haralyzer__ python library https://pypi.org/project/haralyzer/
    from haralyzer import HarParser
and report the result into a program report file.
