# Write a python function that takes a list and returns a new list with unique elements of first list

def unique():
    myList = [1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]
    new_set = set(myList)
    new_tup = tuple(new_set)
    return list(new_tup)

print unique()