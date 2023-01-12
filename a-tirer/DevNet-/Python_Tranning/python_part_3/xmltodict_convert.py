# pip install xmltodict
# 1- OR : from xmltodict import parse
import xmltodict
from pprint import pprint

# 0- OR : xml_example = open("xml_example.xml", "r")
xml_example = open("xml_example.xml").read()
print("------------------------------XML-----------------------------------------")
pprint (xml_example)
print("------------------------------DICT-----------------------------------------")
# 1- OR : xml_dict = parse(xml_example)
xml_dict = xmltodict.parse(xml_example)
pprint (xml_dict)
print("------------------------------INTERFACE LISTE-----------------------------------------")
for interfaces in xml_dict["interface"]["name"]:
    pprint (interfaces)
