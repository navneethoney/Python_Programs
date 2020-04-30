
def primeNumbers(num):
    flag = 0
    list = []

    if num < 2:
        return 0
    elif num >= 2:
        for i in range(2, num):
            for j in range(2, i):
                if (i % j == 0):
                    flag = 1

            if flag == 0:
                list.append(i)
            flag = 0
        print("Prime numbers from 1 to {} = {}".format(num, len(list)))
        return list



print primeNumbers(100)
