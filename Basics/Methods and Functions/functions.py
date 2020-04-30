
def current_place():     # Creating the function
    print("Ottawa")


def current_country(value):  # Parameterized function
    print("Hello "+value)


def addNumbers(num1, num2):  # Function returning values
    num3 = num1 + num2
    return num3  # Only returned value can be assigned to a variable


def say_hello(name = "NAME"):  # If we don't pass an argument in the calling function, we can provide the default value
    print("Hello "+name)

current_place()  # Calling the function
current_country("Canada")
print(addNumbers(2, 5))

say_hello()  # No argument is passed, so it will take "NAME" as the value of argument



# To check if word "dog" is in the string

def dog_check(myString):
    if "dog" in myString:
        return True
    else:
        return False

# OR

def dog_check_2(myString):
    return "dog" in myString  # "dog" in myString itself returns a boolean value, so no need to write if statement

print dog_check("My dog ran away")
print dog_check("My cat ran away")

print dog_check_2("My dog ran away")
print dog_check_2("My cat ran away")



# LEGB (Local, Enclosing function locals, Global (module), Built-in) rule