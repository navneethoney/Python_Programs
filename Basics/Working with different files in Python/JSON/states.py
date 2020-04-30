import json

with open('states.json') as f:
    data = json.load(f)   # json.load(file) lets the json file load into python and we can perform different operations on that

for state in data['states']:
    print(state['name'])

for state in data['states']:
    del state['area_codes']

print data  # This data is to be dumped in a new json file

with open('new_states.json', 'w') as f:  # Dumping the data into new json, 'w' for writing permissions
    json.dump(data, f, indent=2, sort_keys=True)

