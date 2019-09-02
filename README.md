# Final-Project
### Computer Science
##### Uriel Fluss, Levi Dworkin, Ori Moldovan, Yoav Henig
<br />


Measuring QUIC - google new protocol performance compare to known protocols (h2).<br />
<br />
In order to measure the QUIC protocol we need to consider a few things: <br />
- QUIC works only with Google servers and client (Chrome)
- QUIC works with TLS1.3 - all the connections must be with certificates
- To measure QUIC performance we should sniff the data through pcap files or HAR
- The HTTP2.0 scenario should be identical
<br />

We use the *__chrome-har-capturer__* linux command - from
[here][1]
, token from
[these][2]
question.
<br />

To measure the protocol performance we decided to compare 3 things: <br />
- Number of requests
- Total page load time
- Total page and requests weight
All these 3 things can be found in the HAR file. The data analyze from the HAR's files made by the haralyzer python library:<br />
```
from haralyzer import HarParser
```
We extract the results into a program report file.
The data bar chart made with matplotlib python library:<br />

    import matplotlib.pyplot

[1]:https://github.com/cyrus-and/chrome-har-capturer
[2]:https://stackoverflow.com/questions/57081847/export-har-file-using-chrome-quic-protocol-https
