# Sets are unordered collections of unique elements

mySet = set()
print(mySet)

mySet.add(1)
print(mySet)

mySet.add(2)
print(mySet)

mySet.add(2)
print(mySet)

myList = [1, 1, 1, 2, 3, 2, 2, 2, 3, 5.2, 3, 3, 3]
mySet1 = set(myList)  # converting list into set
print(mySet1)