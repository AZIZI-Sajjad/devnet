# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 14:45:20 2021

@author: SDA
"""


"""This script retrieves the list of interfaces from a device using NETCONF
Copyright (c) 2018 Cisco and/or its affiliates.
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


import os
import sys
from ncclient import manager
import xmltodict
import xml.dom.minidom


# Get the absolute path for the directory where this file is located "here"
here = os.path.abspath(os.path.dirname(__file__))

# Get the absolute path for the project / repository root
project_root = os.path.abspath(os.path.join(here, "../.."))


# Extend the system path to include the project root and import the env files
sys.path.insert(0, project_root)

# Create an XML filter for targeted NETCONF queries
netconf_filter = """
<config>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <interface>
      <GigabitEthernet>
        <name xmlns:nc='urn:ietf:params:xml:ns:netconf:base:1.0'>3</name>
        <ip>
          <address>
            <primary>
              <address>192.168.100.1</address>
              <mask>255.255.255.0</mask>
            </primary>
          </address>
        </ip>
        <mop>
          <enabled>false</enabled>
          <sysid>false</sysid>
        </mop>
        <negotiation xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ethernet">
          <auto>true</auto>
        </negotiation>
      </GigabitEthernet>
    </interface>
  </native>
</config>"""


https://www.youtube.com/watch?v=hAuS457449M
https://readthedocs.org/projects/netconf-client/downloads/pdf/stable/
https://dev.to/alecbuda/python-automation-on-cisco-routers-in-2019-netconf-yang-jinja2-52ho
https://www.google.fr/search?q=netconf+python+edit-config+example&sxsrf=AOaemvJy5P8LaAeLbxajh5y9clEqAtTVHg%3A1635758191081&ei=b7B_Yay2BOmFjLsPpseXiA0&oq=netconf+python+edit-config+example&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEM0CMgUIABDNAjIFCAAQzQIyBQgAEM0COgcIABBHELADOgcIIxCwAhAnSgQIQRgAUIhiWMyXAWDxmQFoAXACeACAAWaIAewFkgEDOC4xmAEAoAEByAEIwAEB&sclient=gws-wiz&ved=0ahUKEwjsqauP6vbzAhXpAmMBHabjBdEQ4dUDCA4&uact=5

import env_lab  # noqa

#print("Opening NETCONF Connection to {}".format(env_lab.IOS_XE_1["host"]))

print("IP:{}".format(env_lab.IOS_XE_1["host"]))
print("netconf_port:{}".format(env_lab.IOS_XE_1["netconf_port"]))
print("username:{}".format(env_lab.IOS_XE_1["username"]))
print("password:{}".format(env_lab.IOS_XE_1["password"]))

# Open a connection to the network device using ncclient
with manager.connect(
        host=env_lab.IOS_XE_1["host"],
        port=env_lab.IOS_XE_1["netconf_port"],
        username=env_lab.IOS_XE_1["username"],
        password=env_lab.IOS_XE_1["password"],
        hostkey_verify=False
        ) as m:

    print("Sending a <get-config> operation to the device.\n")
    # Make a NETCONF <get-config> query using the filter
    netconf_reply = m.edit_config(target ='running', config=netconf_filter)


print("Here is the raw XML data returned from the device.\n")
netconf_reply_xml = xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml()
print(netconf_reply_xml)
"""
# Print out the raw XML that returned
print(netconf_reply_xml)
print('*' * 25)

netconf_reply_dict = xmltodict.parse(netconf_reply_xml)

print(netconf_reply_dict)

print('*' * 100)
#print(netconf_reply_xml)
copyToFile = open("DevNet SDA Lab - Get Device's NETCONF - Show Startup-Configuration.txt", "w")
copyToFile.write(netconf_reply_xml)
print('*' * 25)
#m.close_session()
print('Session NETCONF Closed Successfully...')
"""