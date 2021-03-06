# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 22:30:05 2021

@author: SDA
"""


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
url = "https://sandbox-iosxe-latest-1.cisco.com:443/restconf/data/ietf-yang-library:modules-state"

payload={}
headers = {
  'Content-Type': 'application/yang-data+json',
  'Accept': 'application/yang-data+json',
  'Authorization': 'Basic ZGV2ZWxvcGVyOkMxc2NvMTIzNDU='
} 



# verify=False 
# Ignore SSL Certificate verification 
# If is not used 
# response = requests.request("GET", url, headers=headers, data=payload)
#       SSLError: HTTPSConnectionPool(host='10.10.20.48', port=443):
#       Max retries exceeded with url: /restconf/data/ietf-yang-library:modules-state
#       (Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED]
#       certificate verify failed: self signed certificate (_ssl.c:1123)')))
response = requests.request("GET", url, headers=headers, data=payload, verify=False)
print('*' * 100)
print(response.text)
copyToFile = open("DevNet SDA Lab - Get Device's RESTCONF Compatibilities.txt", "w")
copyToFile.write(response.text)


# At the output there are a lot of sectors like follows : 
'''
{
        "name": "CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN",
        "revision": "2000-07-11",
        "schema": "https://10.10.20.48:443/restconf/tailf/modules/CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN/2000-07-11",
        "namespace": "urn:ietf:params:xml:ns:yang:smiv2:CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN",
        "conformance-type": "implement"
      }

----> to Get the information via restconf or configure the equipement, for communicate with Device (login to Device with RESTCONF) 
----> It must modify the URL from https://IP:port/restconf.....
--- in the example, we can change code to :


import requests
import json

url = "https://sandbox-iosxe-latest-1.cisco.com:443/restconf/tailf/modules/CISCO-HSRP-MIB/2010-09-06"

payload={}
headers = {
  'Content-Type': 'application/yang-data+json',
  'Accept': 'application/yang-data+json',
  'Authorization': 'Basic ZGV2ZWxvcGVyOkMxc2NvMTIzNDU='
}

response = requests.request("GET", url, headers=headers, data=payload,verify=False)

print(response.text)
copyToFile = open("DevNet SDA Lab - Get HSRP Status.txt", "w")
copyToFile.write(response.text)

'''