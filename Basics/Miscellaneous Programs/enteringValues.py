x = input("Enter first number ")  # input() function is used to take values from user just like Scanner function in Java
y = input("Enter second number ")  # input() function can only input int
a = int(x)
b = int(y)
p = x + y
z = a + b

print(p)
print(z)

s = raw_input("Enter the value: "); # raw_input() is used to enter the string and int values
print("Value is {}".format(s));

import sys
val1 = int(sys.argv[1])
val2 = int(sys.argv[2])

#sys.argv[] is used to enter the value through command line, for eg, python enteringValues.py 5 6

res = val1 + val2
print(res)