#! C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python310\\python.exe

# import cgi module:
import cgi
import os
os.environ["ProgramFiles"] = 'C:\\Program Files'

from scapy.all import *
from scapy.all import IP

# output http header:
print ('Content-type: text/html')
print ('')
# note the empty print above is required!

print ('<html lang="en"><head><title>NPG</title></head>')
print('<meta charset="UTF-8">')
print('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
print('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">')
print('<link rel="stylesheet" href="http://localhost/NPG/StyleSheets/HomePageStyle.css">')
print ('<body>')
print('''
    <div><div class="row page-header-row"><div class="col-sm-12 text-center page-header">
      <b><a title="NPG" class="hd" href="http://localhost/NPG/HtmlPages/HomePage.html">NETWORK PACKET GENERATOR</a>
                </b>
            </div>

        </div>
    </div>
    <div>
        <marquee class="header-scroll" direction="right" background="#FFFFCC">One stop tool to generate network packects
            using ARP, IP, DNS.</marquee>
    </div>
    <br />
    <br />''')


theRequest = cgi.FieldStorage()
# get the name & sport fields
destinationIP = theRequest.getfirst("destinationIP", "undefined")
dnsQuery = theRequest.getfirst("dnsQuery", "undefined")
sourceIP = theRequest.getfirst("sourceIP", "undefined") 

# Create a DNS query packet
dns_query = IP(dst=destinationIP) / UDP(dport=53) / DNS(rd=1, qd=DNSQR(qname=dnsQuery))

# Send the packet and receive the response
response = sr1(dns_query)

# You can also print the packet to see its structure
if(response) :
    print('<br/>Successfully generated DNS Packet with the specified details, please check in the packet capture tool.')
else:
    print('<br/>Failed to generate DNS Packet with the specified details, please try after sometime.')

print ('</body></html>')



