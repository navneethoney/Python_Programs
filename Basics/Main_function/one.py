
import two

print("Top level in one.py")

two.twoFunction()

if __name__ == '__main__':
    print("one.py is being run directly")
else:
    print("one.py is has been imported")