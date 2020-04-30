firstNum = 1
secondNum = 2

num = input("Please enter the length of series : ")

print(firstNum, secondNum, end= ' ')
for i in range(1, int(num)):
    thirdNum = firstNum + secondNum
    firstNum = secondNum
    secondNum = thirdNum
#
    print(thirdNum, end = " ")

print()
print("*************************************************")

print("Fibonacci series using Recursive Method :", end=' ')

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))

for i in range(int(num)):
    print(fibonacci(i), end=' ');