# In dictionaries, objects are retrieved by key name. Dictionaries are unordered and cannot be sorted.
# In Lists and Tuples, objects are retrieved by location (index value). Ordered sequence can be indexed or sliced.
# All those things are iterable if __iter__ method is present in it

dict = {'name' : 'Navneet',
        'country' : 'Canada',
        'birthPlace' : 'India',
        'yearOfArrival' : 2016}

print(dir(dict))  # To check if dictionary contains __iter__ method, and yes, it is iterable

print(dict)

print(dict['name'])
print(dict['yearOfArrival'])

fruit_prices = {

    'apple' : 2.66,
    'banana' : 0.59,
    'mango' : 1.0,
    'watermelon' : 5.99

}

print("******* ITERATING THROUGH A DICTIONARY ********")
for item in fruit_prices.items():  # We can iterate through a dictionary also
    print(item)
print("******* ITERATION DONE ********")

print(fruit_prices)

print(fruit_prices['mango'])

dict2 = {

    'k1' : 123,
    'k2' : [3, 4, 5, 6],
    'k3' : {
        'insideKey1' : 987,
        'insideKey2' : 789
    }
}

print(dict2)

print(dict2['k2'])
print(dict2['k2'][1])

print(dict2['k3'])
print(dict2['k3']['insideKey1'])

dict2['name'] = 'navneet'  # Adding new value to the dictionary
print(dict2)

dict2['k1'] = "123456"  # Dictionaries are mutable, means values can be changed
print(dict2)

dict3 = {
    'place' : 'Ottawa',
    'country' : 'Canada',
    'year' : 2020
}

list1 = []  # Converts into list
list1.append(dict2)
list1.append(dict3)
print(list1)