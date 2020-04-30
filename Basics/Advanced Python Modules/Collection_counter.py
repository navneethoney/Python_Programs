
from collections import Counter

myList = [1,2,1,1,1,1,2,3,4,5,2,2,2,3,4,5,5,5,5,5,5,5,6,6,7,8,8]

occurances = Counter(myList)
print occurances  # Returns a dictionary

myString = "Mississauga"
occurances = Counter(myString)
print occurances

myWords = "How many times does the words many words how many occur"
occurances = Counter(myWords.split())
print occurances

print(occurances.most_common(2))  # Show me the two most common words
print(sum(occurances.values()))  # Total of all counts
print(list(occurances))  # Lists unique elements
print(dict(occurances))  # Convert to a regular dictionary
print(occurances.items())  # Convert to a list of (element, count) pair
print(occurances.values())
occurances += Counter()  # Remove zero and negative counts