

try:
    f = open('/Users/admin/Downloads/textfile.txt', 'w')
    f.write("Write a test line, hello")
except TypeError:
    print("There was a type error")
except OSError:
    print("Hey, you have an OS error")
except:
    print("All other exceptions")
finally:                                       # finally block always run
    print("I always run")



def ask_a_number():
    while True:
        try:
            result = int(input("Please provide an integer : "))
        except:
            print("This is not a number")
            continue
        else:
            print("Thank you")
            break
        finally:
            print("End of try/except/finally")
            print("I will always run at the end")


ask_a_number()