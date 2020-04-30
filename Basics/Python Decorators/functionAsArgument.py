
def hello():
    return "Hi Jose"


def other(some_def_func):
    print("Other code runs here")
    print(some_def_func())


other(hello)  # We can also pass the function as an argument