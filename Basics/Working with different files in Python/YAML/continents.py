import yaml
import json
import re

# Convert yaml into python dictionary
with open("continents.yaml", "r") as PyContinents:
    Pydata = yaml.load(PyContinents, Loader= yaml.FullLoader)
    print Pydata


# Convert yaml into json
with open("continents.yaml", "r") as YamlContinents:  # Reading/loading data from yaml
    data = yaml.load(YamlContinents, Loader= yaml.FullLoader)
    with open("continent.json", "w") as JsonContinents:  # Writing loaded yaml data in json
        json.dump(data, JsonContinents, indent=2)


# Printing all the states of India
for states in Pydata['Continents'][0]['Asia'][0]['India']:
    print states


for europe in Pydata['Continents'][3]['Europe']:
    my_list = []
    my_list.append(europe)
    print my_list[0]  # With the help of regular expressions, we can extract 'London' out of this string
    break