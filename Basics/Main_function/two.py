
def twoFunction():
    print("two.py file is running")

print("Top level in two.py")

if __name__ == '__main__':
    print("two.py is being run directly")
    twoFunction()
else:
    print("two.py has been imported")