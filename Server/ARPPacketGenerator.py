#! C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python310\\python.exe

# import cgi module:
import cgi
import os
os.environ["ProgramFiles"] = 'C:\\Program Files'

import scapy.all as scapy

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
destinationMAC = theRequest.getfirst("destinationMAC", "undefined")
sourceIP = theRequest.getfirst("sourceIP", "undefined")



# Create an ARP request packet
arp_packet = scapy.ARP(
    op=1,  # 1 for ARP request, 2 for ARP reply
    pdst=destinationIP,  # Destination IP address
    hwdst=destinationMAC,  # Destination MAC address
    psrc=sourceIP  # Source IP address
)

# Send the ARP request packet
response = scapy.send(arp_packet) 

# You can also print the packet to see its structure
if(arp_packet) :
    print('Successfully generated ARP Packet with the specified details, please check in the packet capture tool.')
else:
    print('Failed to generate ARP Packet with the specified details, please try after sometime.')

print ('</body></html>')

