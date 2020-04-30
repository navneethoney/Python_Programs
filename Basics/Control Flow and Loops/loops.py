list1 = [1, 2, 3, "navneet", 6.3, 7]

for i in list1:   # Good way of implementing for loop
    print(i)

print("******************************")

# OR
for i in range(0, len(list1)):  # Traditional for loop
    print(list1[i])


print("To print even and odd numbers in the list:")
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

for num in list2:
    if (num % 2 == 0):
        print("Even number = {}".format(num))
    else:
        print("Odd number = {}".format(num))

sum = 0
for num in list2:
    sum = sum + num

print("Sum of all the numbers in the list = {}".format(sum))


tup = (1, 2, 3, 4)

for i in tup:
    print(i)


my_list = [(1, 2), (3, 4), (5, 6), (7, 8)]  # List can contain Tuples and vice versa

for item in my_list:
    print(item)


for (a, b) in my_list:  # Tuple unpacking
    print(a)
    print(b)

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

my_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

for a, b, c in my_list:
    print b


# Iterating for loop in dictionary

dict = {
    'k1' : 1,
    'k2' : 2,
    'k3' : 3,
    'k4' : 4
}

for key, value in dict.items():
    print(value)  # 3, 2, 1, 4 (unordered)

# OR

for val in dict.values():
    print(val)


x = 0

while(x <= 5):
    print("Hello world {}".format(x))
    x = x + 1
else:
    print("x is greater than 5")


y = [1, 2, 3, 4, 5]

for i in y:
    pass

print("End of my script")

myString = "Sammy"

for letter in myString:
    if letter == 'a':
        continue  # Reinitiate the loop instead of printing the letter
    print(letter)  # S m m y


for letter in myString:
    if letter == 'a':
        break  # Terminating the loop
    print(letter)  # S


word = 'abcde'

for item in enumerate(word):
    print(item)  # returns tuple

for index, letter in enumerate(word):
    print(index)
    print(letter)


myList1 = [1, 2, 3, 4, 5]
myList2 = ['a', 'b', 'c']
myList3 = [100, 200, 300]

for item in zip(myList1, myList2, myList3):
    print(item)

if x in myList2:
    print("x is there")
else:
    print("x is not in the list")

dict = {
    'k1' : 123,
    'k2' : 456
}

if 123 in dict.values():
    print("True")
else:
    print("False")


# NOTE
# values() only returns values corresponding to the keys in dictionary
# items() returns both key and value pairs

