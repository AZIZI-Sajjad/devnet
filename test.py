#!/usr/bin/env python
import sys
from argparse import ArgumentParser
from ncclient import manager

import xml.dom.minidom

config = '''
<config
	xmlns:xc="urn:ietf:params:xml:ns:netconf:base:1.0">
	<native
		xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
		<interface>
			<GigabitEthernet>
				<name>3.121</name>
				<encapsulation>
					<dot1Q>
						<vlan-id>121</vlan-id>
					</dot1Q>
				</encapsulation>
				<ip>
					<address>
						<primary>
							<address>169.254.121.254</address>
							<mask>255.255.255.252</mask>
						</primary>
					</address>
				</ip>
				<logging>
					<event>
						<link-status/>
					</event>
				</logging>
				<description>This is my new GigabitEthernet description!</description>
			</GigabitEthernet>
		</interface>
	</native>
</config>
'''
        
if __name__ == '__main__':
    
    # parser = ArgumentParser(description='Select options.')

    # # Input parameters
    # parser.add_argument('--host', type=str, required=True,
    #                     help='The device IP or DN. Required')
    # parser.add_argument('-u', '--username', type=str, required=True,
    #                     help='Username on the device. Required')
    # parser.add_argument('-p', '--password', type=str, required=True,
    #                     help='Password for the username. Required')
    # parser.add_argument('--port', type=int, default=830,
    #                     help='Specify this if you want a non-default port. Default: 830')
    
    # args = parser.parse_args()

	
    with manager.connect(host='sandbox-iosxe-latest-1.cisco.com',
                        port=830,
                        username='developer',
                        password='C1sco12345',
                        hostkey_verify=False) as m:
        
        with m.locked(target='running'):
            m.edit_config(target='running', config=config)

            print('Successfully applied configuration update. Issue get-config to verify changes')
