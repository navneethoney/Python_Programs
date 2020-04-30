def upperLower(s):
    count = 0
    count1 = 0
    for i in s:
        if i >= 'A' and i <= 'Z':
            count = count + 1
        elif i >= 'a' and i <= 'z':
            count1 = count1 + 1

    print("No. of Upper case letters = {}".format(count))
    print("No. of Lower case letters = {}".format(count1))



upperLower("Hello Mr.Rogers, how are you this fine Tuesday")