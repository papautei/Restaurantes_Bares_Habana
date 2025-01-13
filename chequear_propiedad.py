import os
import json
from methods import datastorage

data = datastorage("JsonData")

PropertyType = {}
NoneProperty = []

for file in data:
    if data[file]["Ownership"] in PropertyType:
        PropertyType[data[file]["Ownership"]] += 1
    else:
        PropertyType[data[file]["Ownership"]] = 1
    if data[file]["Ownership"] == None:
        NoneProperty.append(file)

print(json.dumps(PropertyType, indent=3))
#print(json.dumps(NoneProperty, indent=3))

