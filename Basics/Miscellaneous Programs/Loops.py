i = 1

while(i <= 5):
    print("Navneet "+ str(i))
    i = i + 1


j = 5

while(j >= 1):
    print("Honey "+ str(j))
    j = j - 1

print("*********************************************")

p = 1

while(p <= 5):
    print("Navneet p = {}".format(p))
    q = 1
    while(q <= 4):
        print("Honey q = {}".format(q))
        q = q + 1

    p = p + 1

print("****************************************")

x = ["navneet", 27, 5.5]  # We can store anything in a list
print(x)

for i in x:
    print(i)

y = "Canada"
for i in y:
    print(i)

for i in [2, 4.5, "honey"]:
    print(i)


for i in range(0, 10):
    print(i)


for i in range(10, 100, 5):
    print(i)

for i in range(11, 20, -1):
    print(i)

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

for i in range(1, 31):
    if(i % 5 != 0):
        print(i)


num = 1
num = "one"

print(num)