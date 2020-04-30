# JSON = JavaScript object notation

'''

JSON                Python
object -->          dict
array -->           list
string -->          str
number (int) -->    int
number (real) -->   float
true -->            True
false -->           False
null -->            None

'''

import json, ast

dumps = json.dumps(['foo', {'bar' : ('baz', None, 1.0, 2)}])  # Json encoder

print dumps

loads = json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')  # Json decoder

print loads

# This is JSON:

people_string = '''
{
    "people" : [
    {
        "name" : "John Smith",
        "phone" : "615-555-7164",
        "emails" : ["johnsmith@bogusemail.com", "john.smith@work-place.com", "john_smith@fakeemail.com"],
        "has_license" : false
    },

    {
        "name" : "Jane Doe",
        "phone" : "505-555-5153",
        "emails" : null,
        "has_license" : true
    }
]
}
'''

# Dictionaries contain mixed values of string, float, int, list, dictionary, boolean........everything


data = json.loads(people_string)   # Now data is a dictionary
print(type(data))  # Type is dict
print(data)
print("**********")
print(data['people'][0])  # Possible only if JSON returns a Dictionary in Python
print(type(data['people']))  # Type is list
print(data['people'][0]['phone'])
print(data['people'][0]['name'])
print(data["people"][0]['has_license'])  # False in python
print(data['people'][0]['emails'][1])

for person in data['people']:
    print(person['name'])


for email in data['people']:
    first_email = email['emails']
    break
print first_email[0]
print first_email[2]

'''
To remember:
json.loads converts JSON into dictionary
json.loads takes a string, it does not takes the file path
json.load converts JSON into python object, json.load accepts a file object
json.dumps converts JSON into string (dump 's' for string)
json.dump dumps the data into a new file

'''
# To delete phone numbers of each person and convert it back to json
# Removing phone numbers from dictionary

for person in data['people']:
    del person['phone']

new_string = json.dumps(data, indent=2, sort_keys=True)  # indent for proper indentation, sort_keys sorts alphabetically
print new_string