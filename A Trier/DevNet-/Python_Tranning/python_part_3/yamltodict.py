# pip install PyYAML
import yaml
from pprint import pprint

yaml_example = open("yaml_example.yaml").read()
#yaml_example = open("yaml_example.yaml", "r")
print("------------------------------YAML-----------------------------------------")
pprint (yaml_example)
print("------------------------------DICT-----------------------------------------")
yaml_dict = yaml.load(yaml_example)
pprint (yaml_dict)
print("-------------INTERFACE LISTE + Enabled (True / False)-----------------------")
for interfaces in yaml_dict["ietf-interfaces:interfaces"]:
    pprint (interfaces["name"]+": "+ str(interfaces["enabled"]))
print("-------------------------INTERFACE STATUS-----------------------------------")
for interfaces in yaml_dict["ietf-interfaces:interfaces"]:
    if str(interfaces["enabled"])  == "False":
        pprint (interfaces["name"]+":   "+ "Disbled")
    if str(interfaces["enabled"])  == "True":
        pprint (interfaces["name"]+":   "+ "Enabled")
