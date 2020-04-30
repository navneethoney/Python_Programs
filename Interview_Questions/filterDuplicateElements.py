
elements = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5, 6, 6, 7];

duplicate_elements = []

ele = set(elements)
list_distinct = list(ele)
print ("List of distinct elements = {}".format(list_distinct))

count = 0;

for i in list_distinct:
    for j in elements:
        if(i == j):
            count+=1;

    if(count > 1):
        duplicate_elements.append(i)
    count = 0

print("List of duplicate elements : {}".format(duplicate_elements))


