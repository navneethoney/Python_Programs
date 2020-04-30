
# To create a new text file:

f = open("new_text_file.txt", "w+")  # This is to create a new text file, w+ is for writing into a text file

for i in range(10):
    f.write("This is the line {} \n".format(i))  # Writing data into the text file

f.close()  # Closing the file is very important

# OR
# Another way of writing the file

ocean = ['Pacific', 'Atlantic', 'Indian', 'Arctic', 'Southern']

with open("new_textfile_without_close_fnc", "w") as new:  # No need to close the file using this
    for items in ocean:
        new.write("This is ocean {} \n".format(items))


# To append data into a file :

f = open("new_text_file.txt", "a+")

for i in range(3):
    f.write("Appended line {} \n".format(i))

f.close()

# OR

with open("new_textfile_without_close_fnc", "a") as foo:
    for i in range(2):
        foo.write("Appended line {} \n".format(i))


# To read the contents of the file:

f = open("new_text_file.txt", "r")
text = f.read()
f.close()  # We have always to close the file at the end using this method

print(text)

# OR

# This is the best way to read the file and we need not to close it at the end. Python will close the file even if exception occurs in code

with open("new_text_file.txt", "r") as foo:
    txt = foo.read()


print(txt)
print(foo.name)
print(foo.mode)
print(foo.closed)

with open("new_text_file.txt", "r") as p:
    for line in p:
        print(line)

    # txt1 = p.readlines()  # It will return the text lines in the form of list
    # print(txt1, end = '')


with open("new_text_file.txt", "r") as rf:
    with open("test_copy.txt", "w") as wf:
        for line in rf:
            wf.write(line)  # Created a new file "test_copy.txt and copied all the lines from new_text_file.txt

# To copy the pictures, we need 'rb', 'wb' instead of 'r' and 'w' where b stands for binary