# To check if digits are present in a String

val =  "hello10world";

def hasNumber():
    for i in val:
        if(i.isdigit()):
            return True

if(hasNumber()):
    print("Digit is present")
else:
    print("All Characters")