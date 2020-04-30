# ABCDDCBA

def palindrome(s):
    string_one = s[:(len(s))/2]
    string_two = s[(len(s))/2:]
    string_invert = string_two[::-1]

    if string_one == string_invert:
        print("String is Palindrome")
    else:
        print("String is not Palindrome")


palindrome('helleh')


# OR

def palindrome_func(s):
    return s == s[::-1]

print palindrome_func('helleh')