# List is mutable

my_list = [1, 2, 3]
print(my_list)

my_list = ['String', 3, 4.2]
print(my_list)

print(len(my_list))

print(my_list[0])

list1 = ['one', 'two', 'three']
list2 = ['four', 5]

new_list = list1 + list2
print(new_list)

print(new_list[1:])  # Slicing

list1[0] = "ONE ALL CAPS"
print(list1)

list2.append("six")
print(list2)

list1.pop()
print(list1)  # pop() removes the last element of the list

long_list = [1, "two", 3.3, 4, "FIVE", 6, "Seven"]
popped_value = long_list.pop(3)  # Removes element from specific index
print(long_list)
print("Popped value is = {}".format(popped_value))

new_alphabet_list = ['a', 'i', 'e', 'u', 'o']
new_alphabet_list.sort()
print (new_alphabet_list)

num_list = [3, 5, 1, 8 ,6, 2]
num_list.sort()
print(num_list)

num_list.reverse()   # Reversing the list
print(num_list)


list3 = [9, 8, 'seven', 6]
list3[2] = 7
print(list3)   # LISTS ARE MUTABLE

my_list = list(range(0, 11, 2))  # This is generating even numbers and casted into a list
print(my_list)


myList = ['a', 'b', 'c']  # To join the list
joined_list = "--".join(myList)
print joined_list

joined_list = "".join(myList)
print joined_list

l = [1, 2, 3, 4, 5]
x = l.extend([6, 7])
print l