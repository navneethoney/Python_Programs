
def addNums(n1, n2):
    return n1 + n2

print addNums(10, 20)

# print addNums(50, "Please provide a number")  # Error
# print "Hello world"  # This statement will not be executed because of error in above line

try:
    # Want to attempt this code, May have an error
    result = 10 + '10'
except:
    print("Looks like you aren't adding correctly")  # If there is an error, except block executes
else:
    print("Add went well")
    print(result)

print("Hello world")  # This will run because error is handled in above code