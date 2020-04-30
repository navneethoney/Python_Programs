import re

# search method will scan the text and match the pattern
patterns = ['term1', 'term2']
text = "This is a string with term1, but not the other term"

for pattern in patterns:

    print("Searching for {} in: \n{} \n".format(pattern, text))
    print("Result = ")

    if re.search(pattern, text):
        print("Match found")
    else:
        print("No match found")

print("*************************************************************")

phrase = "What is your email, is it hello@gmail.com?"
print(phrase.split("@"))

# OR

split_term = "@"
print re.split(split_term, phrase)

print("**********************************************************")

matchFind = re.findall("match", "Here is one match, here is another match")
print(matchFind)  # Returns a list of all matches
print(len(matchFind))  # Returns number of matches

print("************************************************************")

def multi_re_find(patterns, sentence):

    for pattern in patterns:
        print("Searching the phrase using re check : '{}'".format(pattern))
        print re.findall(pattern, sentence)

test_phrase = "sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd"
test_patterns = ['sd*', 'sd+', 'sd?', 'sd{3}', 'sd{2,3}', '[sd]', 's[sd]+']

print(multi_re_find(test_patterns, test_phrase))

'''

'sd*' --> s followed by zero or more d's
'sd+' --> s followed by one or more d's
'sd?' --> s followed by zero or one d's
'sd{3}' --> s followed by three d's
'sd{2,3}' --> s followed by two or three d's
'[sd]' --> Either s or d
's[sd]+ --> s followed by one or more s or d

'''

print("*******************************************************************")

test_line = "This is an example sentence. Lets see if we can find some letters"
test_patterns = ['[a-z]+', '[A-Z]+', '[a-zA-Z]+', '[A-Z][a-z]+']

multi_re_find(test_patterns, test_line)

'''
'[a-z]+' --> Sequence of lower case letters
'[A-Z]+'  --> Sequence of upper case letters
'[a-zA-Z]+' --> Sequence of lower or upper case letters
'[A-Z][a-z]+'  --> One upper case letter followed by lower case letters

'''
print("********************************************************************")

test_phrase = 'This is a string with some numbers 1233 and a symbol #hashtag'
test_patterns = [r'\d+', r'\D+', r'\s+', r'\S+', r'\w+', r'\W+']

multi_re_find(test_patterns, test_phrase)

'''
r'\d+' --> Sequence of digits
r'\D+' --> Sequence of non-digits
r'\s+' --> Sequence of whitespace
r'\S+' --> Sequence of non-whitespace
r'\w+' --> Alphanumeric characters
r'\W+' --> Non-alphanumeric

'''