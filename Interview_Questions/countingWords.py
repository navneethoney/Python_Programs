
from collections import Counter;
val = "Let come back to the topic of the day to come come";

val1 = val.split();
val2 = Counter(val1);
print val2

print("Most commonly occuring word : {}".format(val2.most_common(1)))
print("2 most commonly occuring words : {}".format(val2.most_common(2)))

unique = set(val1)
list_unique = list(unique)
print list_unique



# OR

count = 0
for i in list_unique:
    for j in val1:
        if(i == j):
            count+=1;

    print("Count of {} is {}".format(i, count))
    count = 0
