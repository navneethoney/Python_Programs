
for num in range(1, 101):
    if(num % 3 == 0 and num % 5 == 0):
        print("PingPong");
    elif(num % 3 == 0):
        print("Ping");
    elif(num % 5 == 0):
        print("Pong");