import requests
import json



# CISCO SandBox Router Allways ON  :
# '''https://devnetsandbox.cisco.com/RM/Diagram/Index/7b4d4209-a17c-4bc3-9b38-f15184e53a94?diagramType=Topology'''
# R1000v Host: sandbox-iosxe-latest-1.cisco.com
# H Port: 22
# NETCONF Port: 830
# gRPC Telemetry Port: 57500
# RESTCONF Port: 443 (HTTPS)
# Username: developer
# Password: C1sco12345
# --> NOT UDES HERE
#
#

# OR
# 
# # 
# CISCO SandBox Lab "IOS XE on CSR Latest Code" :
# https://devnetsandbox.cisco.com/RM/Diagram/Index/f864352b-f562-44b1-ad24-5f01aa34cfa1
# First reserve the Lab then connect to Lab's VPN then :
# I used this lab : 
url = "https://10.10.20.48:443/restconf/data/ietf-interfaces:interfaces"

payload = json.dumps({
  "ietf-interfaces:interface": {
    "name": "Loopback100",
    "description": "Configured by RESTCONF - SDA ",
    "type": "iana-if-type:softwareLoopback",
    "enabled": True,
    "ietf-ip:ipv4": {
      "address": [
        {
          "ip": "169.254.254.1",
          "netmask": "255.255.255.255"
        }
      ]
    }
  }
})
headers = {
  'Authorization': 'Basic ZGV2ZWxvcGVyOkMxc2NvMTIzNDU=',
  'Accept': 'application/yang-data+json',
  'Content-Type': 'application/yang-data+json'
}



# verify=False
# Ignore SSL Certificate verification 
# If is not used 
# response = requests.request("GET", url, headers=headers, data=payload)
#       SSLError: HTTPSConnectionPool(host='10.10.20.48', port=443):
#       Max retries exceeded with url: /restconf/data/ietf-yang-library:modules-state
#       (Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED]
#       certificate verify failed: self signed certificate (_ssl.c:1123)')))

# 
# GET  : 
#   Is for getting information from Device 
# POST : 
#   Is for write changes to Device 

response = requests.request("POST", url, headers=headers, data=payload, verify=False)

print(response.text)
