
# "*" accepts number of arguments, hence we need not to write many arguments in a function, rather it forms a tuple
# which can accept infinite number of arguments

#Traditional way:

def myfun(a, b, c, d, e):
    return sum((a, b, c, d, e)) * 0.05

# New way:

def myfunc(*args):  # *args used to accept infinite number of arguments
    return sum(args) * 0.05

def myNewFunc(*args):
    for item in args:
        print item

print myfun(1, 2, 5, 7, 10)
print myfunc(2, 4, 5, 7, 5, 7, 9, 3, 100)
myNewFunc(10, 20, 30, 40, 55, "Navneet")  # It returns a tuple


def myfunc_new(**kwargs):  # "**" returns a dictionary, but convention, we should always use kwargs
    print(kwargs)
    if "fruit" in kwargs:
        print("My fruit choice is {}".format(kwargs['fruit']))
    else:
        print("I didn't find any fruit here")

myfunc_new(fruit = "apple", veg = "lettuce")


def printText(*args, **kwargs):
    print args
    print kwargs
    print ("I would like {} {}".format(args[0], kwargs['fruit']))

# args forms a tuple, so we are grabbing first value of tuple, ie, 10
# kwargs forms a dictionary, so we are grabbing the value of food

printText(10, 20, 30, food = "rice", fruit = "mango", diet = "vegetarian", country = "Canada")


# Program:
def evenNumbers(*args):
    new_list = []
    for i in args:
        if (i % 2 == 0):
            new_list.append(i)
    return new_list

print evenNumbers(2, 3, 4, 5, 6, 7)

# Program:

def upperLower(st):
    mylist = list(st)
    new_list = []

    for i in range(0, len(mylist)+1):
        if (i % 2 == 0):
            new_list.append(mylist[i])
    print new_list

upperLower("NavneetSinghChhabra")