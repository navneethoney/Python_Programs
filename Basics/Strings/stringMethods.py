name = "navneet"
# make it tavneet

# name[0] = 't'  Strings are immutable, can't assign any new character to a string character
s = name[1:]
print('t'+s)

print('2'+'4')
print(int('2')+int('5'))

x = 'canada snowfall'
print(x.upper())
print(x)
print(x.capitalize())

print(x.split()) # Splitting string and converting into a list
print(x.split('a'))

name = 'Jose'
print('San ' + name)


# STRING FORMATTING :

print("This is {}".format("Canada"))
print("I am from {}, came to {} in {}".format("India", "Canada", "2016"))
print("My name is {0} {1} {0}".format("Navneet", "Singh"))
print("I am {l} {p} from {u}".format(p = "python", l = "learning", u = "Udemy"))

result = 100.0/777
print(result)
print("The result was {r}".format(r = result))
print("The result was {r:1.3f}".format(r = result))  # value:width.precision f
print("The result was {r:10.3f}".format(r = result))  # It will leave white space

name = "navneet singh"
country = "India"
print("My name is {} from {}".format(name, country))