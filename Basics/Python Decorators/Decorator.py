
def new_decorator(original_func):

    def wrap_func():

        print("Some extra code, before the original function")

        original_func()

        print("Some extra code, after the original function !")

    return wrap_func()


def func_needs_decorator():
    print("I want to be decorated !!")


decorated_func = new_decorator(func_needs_decorator)  # Function passed as an argument
decorated_func


print("*******************************************************************************")

@new_decorator  # This is automatically wrapping the entire function
def func_needs_decorator():
    print("I want to be decorated !!")

func_needs_decorator # It is doing the same thing