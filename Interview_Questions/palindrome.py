
text = raw_input("Please enter the String : ")

part1 = text[:len(text)/2]
part2 = text[len(text)/2:]
part2_invert = part2[::-1]

if part1 == part2_invert:
    print "String is Palindrome"
else:
    print "String is not Palindrome";