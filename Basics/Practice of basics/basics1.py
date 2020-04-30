# Basic concepts of Python

print("**************** Hello World ************************")
print("hello world")
print("hello world")
print("hello world")
print("hello world")

print("***************** For Loop ***********************")

for i in range(0, 5):
    print("Hello for loop {}".format(i));

print("*************** While Loop *************************")

i = 0;
while(i < 5):
    print("Hello while loop {}".format(i))
    i +=1;

print("****************** If Else Statement **********************")

a = 11;
if(a < 10):
    print("a is less than 10")
elif(a > 10):
    print("a is greater than 10")
else:
    print("a is equal to 10");

print("**************** Inputting the String ************************")

# x = raw_input("Enter the value: ")  # raw_input() function is used to enter both string and int values
# print("Value is {}".format(x));


print("**************** Reverse of a String ************************")

str1 = "ABCDE";

print(str1[::-1]);

str2 = "EDCBA";
if(str1 == str2[::-1]):
    print("Strings are Pallindrome");
else:
    print("Strings are not Pallindrome")

print("**************** Pallindrome ************************")

str3 = "ABCDEDCBA";
str4 = str3[::-1];


if(str3[:len(str3)/2] == str4[:len(str4)/2]):
    print("String is Pallindrome -- ");
else:
    print("String not pallindrome -- ");

