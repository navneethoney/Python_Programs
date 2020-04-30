
class Book:

    def __init__(self, title, author, pages):  # Constructor
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):  # this should only return string
        return ("{} by {}".format(self.title, self.author))

    def __len__(self):  # this should only return int
        return self.pages

    def __del__(self):  # To print the report of delete
        print("A book object has been deleted")


b = Book("Python rocks", "Jose", 200)
print(b)  # Output = <__main__.Book instance at 0x105446290>
print(str(b))  # Output is the string version of above

print(b)  # Output = Python rocks by Jose
print(len(b))

del b  # Deleting b from the memory