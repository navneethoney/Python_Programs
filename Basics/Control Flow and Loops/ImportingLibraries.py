from random import shuffle

myList = [1, 2, 3, 4, 5]

shuffle(myList)

print(myList)

from random import randint

num = randint(0, 100)

print(num)

result = input("Enter the number: ")  # input() function accepts input from the user, always in the form of int

print("The number entered is {}".format(result))

myList1 = [x for x in "word"]  # shortcut. It is called list Comprehension
print(myList1)

# OR

myList2 = []
myString = "hero"

for letters in myString:
    myList2.append(letters)
print(myList2)

myList3 = [num**2 for num in range(0, 11)]
print(myList3)