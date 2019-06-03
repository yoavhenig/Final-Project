# Final-Project
### Computer Science final project
##### Uriel Fluss, Levi Dworkin, Ori Moldovan, Yoav Henig
<br />
Measuring QUIC - google new protocol performance compare to known protocols (h2..).<br />
<br />
We use __selenium__ python library https://pypi.org/project/selenium/ to open chrome and navigate through the internet.

    from selenium import webdriver
__browsermob-proxy__ python library https://pypi.org/project/browsermob-proxy/ to export the sniffing data into HAR file.<br />

    from browsermobproxy import Server 
To analyze network traffic reported in the HAR file we use __haralyzer__ python library https://pypi.org/project/haralyzer/.

    from haralyzer import HarParser
We extract the results into a program report file.
