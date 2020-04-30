a = 10
b = 20

if(a < b):
    print("a is less than b")
elif(a > b):
    print("a is greater than b")
else:
    print("program ends")

print("Bye")


num = int(input("Enter the number : "))

if(num % 2 == 0):
    print("Number is Even")
    if(num > 3):  # Nested if statement
        print("Number is greater than 3")
    else:
        print("Number is not greater than 3")

else:
    print("Number is odd")