# New Python Concepts

print("**************** Find unique numbers in list ************************")

normal_list = [1, 1, 1, 3, 5, 2, 2, 3, 2, 2, 5, 5, 5, 6];
unique_set = set(normal_list);
unique_tuple = tuple(unique_set);
print(unique_tuple)

print("**************** Inputting values ************************")
# Uncomment the code to run

# s = raw_input("Enter the value: "); # raw_input() is used to enter the string or int values
# print("Value is {}".format(s));

print("**************** Reversing the numbers using range function ************************")
for k in range(10, 0, -1):
    print k

for k in range(10, 0, -2):  # 2 steps back
    print k


print("**************** Functions ************************")

def writeName(fullName="Nav Singh"):  # If we don't pass an argument in the calling function, we can provide the default value
    print("Hello "+fullName);

writeName();

str = "Hello, I live in Canada";

print("**************** String checks ************************")

if "live" in str:
    print("Yes");
else:
    print("No");

def check_animal(animal):
    return "dog" in animal;

print(check_animal("zebra, dog, cat, cow, giraffe"));

print("**************** ARGS and KWARGS ************************")

def infinite_args(*args):  # *args is used to accept infinite number of arguments
    print(args);  # Returns a tuple

infinite_args(1, 2, 3, 4, "hello", {'name': 'navneet'});

def items_enter(*args):
    for item in args:
        print item;

items_enter(1, 4, "hello", "Canada", 5.6);

def perform(**kwargs):
    print(kwargs);
    if 'firstName' in kwargs:
        print ("First name is = {}".format(kwargs['firstName']));
    else:
        print 'no'

perform(firstName= 'navneet', lastname= 'Singh', place= 'Canada');

print("**************** List ************************")

list1 = [1, 5, 9, 2, 6];  # Reversing the list
list1.reverse();
print(list1);

my_list = list(range(0, 11, 2))  # This is generating even numbers and casted into a list
print(my_list);

myList = ['a', 'b', 'c']  # To join the list
joined_list = "--".join(myList)
print joined_list

joined_list = "".join(myList)
print joined_list

print("**************** Tuples ************************")

tup = ('a', 'a', 'b')
print(tup.count('a'))  # Count the number of 'a'
print(tup.index('a'))

print("**************** Object Oriented ************************")

class Values:

    def __init__(self, name, city, age):
        self.naam = name;
        self.shehar = city;
        self.umar = age;

    def __str__(self):  # Special method
        return("{} belongs to {}".format(self.naam, self.shehar));

    def __len__(self):  # Special method
        return self.umar;


val = Values("Navneet", "Montreal", 28);
print(val.naam);
print(val.shehar);
print(val);  # This will hit the __str__ method
print(val.umar);

print("**************** Iterating through dictionary using 'for' loop ************************")

dict = {
    'k1' : 1,
    'k2' : 2,
    'k3' : 3,
    'k4' : 4
}

for key, value in dict.items():
    print(value);  # Unordered values of dictionary

for val in dict.values():
    print(val);   # Unordered values of dictionary

# values() only returns values corresponding to the keys in dictionary
# items() returns both key and value pairs

print("**************** Skip the block/loop ************************")

y = [1, 2, 3, "navneet", 4.9]

for i in y:
    pass

print("**************** Continue clause ************************")

for letter in "Navneet":
    if letter == 'a':
        continue  # Reinitiate the loop instead of printing the letter
    print(letter)  # N v n e e t

print("**************** Break clause ************************")

for letter in "Navneet":
    if letter == 'a':
        break  # Terminating the loop
    print(letter)  # N

print("**************** Zipping the list ************************")

myList1 = [1, 2, 3, 4, 5]
myList2 = ['a', 'b', 'c']
myList3 = [100, 200, 300]

for item in zip(myList1, myList2, myList3):
    print(item)

print("**************** Getting the random number ************************")

from random import randint;

num = randint(0, 100);
print("Random number is : {}".format(num));

print("**************** Ways of using format method ************************")

print("Location is {} in {}, {}".format("Ottawa", "Ontario", "Canada"));
print("My name is {0} {1} {0}".format("Navneet", "Singh"));  # Re-using the values instead of writing again and again
print("I am {l} {p} from {u}".format(p = "python", l = "learning", u = "Udemy"))

result = 100.0/777
print(result)  # 0.1287001287
print("The result was {r}".format(r = result))
print("The result was {r:1.3f}".format(r = result))  # value:width.precision f     "0.129"
print("The result was {r:10.3f}".format(r = result))  # It will leave white space

print("********************************* Look at Advanced python modules ******************************")

