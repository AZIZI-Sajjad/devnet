#!/usr/bin/env python
"""This script adds a new loopback to a device using NETCONF.

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
import env_lab  # noqa

print('*' * 20)
print(env_lab.IOS_XE_2["host"])
print('*' * 20)
# IETF Interface Types
IETF_INTERFACE_TYPES = {
        "subinterface": "ianaift:ethernetCsmacd",
        "ethernet": "ianaift:ethernetCsmacd"
    }

# Create an XML configuration template for ietf-interfaces
netconf_interface_template = """
<config xmlns:xc="urn:ietf:params:xml:ns:netconf:base:1.0">
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <interface>
      <GigabitEthernet>
        <name>3</name>
        <description>This is my new GigabitEthernet description!</description>
        <enabled>true</enabled>
            <ipv4>
                <address>
                    <ip>169.254.136.254</ip>
                    <netmask>255.255.255.252</netmask>
                </address>
            </ipv4>
      </GigabitEthernet>
    </interface>
  </native>
</config>
"""

# Ask for the Interface Details to Add 
# new_subinterface = {}
# new_subinterface["name"] = "GigabitEthernet" + input("What subinterface number to add? ")
# new_subinterface["desc"] = input("What description to use? ")
# new_subinterface["type"] = IETF_INTERFACE_TYPES["subinterface"]
# new_subinterface["status"] = "true"
# new_subinterface["ip_address"] = input("What IP address? ")
# new_subinterface["mask"] = input("What network mask? ")

# Create the NETCONF data payload for this interface2.222
# netconf_data = netconf_interface_template.format(
#         name = new_subinterface["name"],
#         desc = new_subinterface["desc"],
#         type = new_subinterface["type"],
#         status = new_subinterface["status"],
#         ip_address = new_subinterface["ip_address"],
#         mask = new_subinterface["mask"]
#     )

print("The configuration payload to be sent over NETCONF.\n")
# print(netconf_data)

print("Opening NETCONF Connection to {}".format(env_lab.IOS_XE_2["host"]))

# Open a connection to the network device using ncclient
with manager.connect(
        host=env_lab.IOS_XE_2["host"],
        port=env_lab.IOS_XE_2["netconf_port"],
        username=env_lab.IOS_XE_2["username"],
        password=env_lab.IOS_XE_2["password"],
        hostkey_verify=False
        ) as m:

    print("Sending a <edit-config> operation to the device.\n")
    # Make a NETCONF <get-config> query using the filter
    netconf_reply = m.edit_config(netconf_interface_template, target = 'running')

print("Here is the raw XML data returned from the device.\n")
# Print out the raw XML that returned
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
print("")
