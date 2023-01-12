# pip install jason
import json
from pprint import pprint

# OR : xml_example = open("jason_example.xml", "r")
json_example = open("json_example.json").read()
print("------------------------------JASON-----------------------------------------")
pprint (json_example)
print("------------------------------DICT-----------------------------------------")
json_dict = json.loads(json_example)
pprint (json_dict)
print("-------------------------INTERFACE LISTE------------------------------------")
for interfaces in json_dict['ietf-interfaces:interface']:
    print (interfaces)
