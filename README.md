# Final-Project
### Computer Science final project
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

    from haralyzer import HarParser
We extract the results into a program report file.

[1]:https://github.com/cyrus-and/chrome-har-capturer
[2]:https://stackoverflow.com/questions/57081847/export-har-file-using-chrome-quic-protocol-https
