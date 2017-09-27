# exceptions are written a lot like they are in Java; with a try/except/finally block
# try
#   - code -
# except IOError:
#   - code -
# except ValueError:
#   - code -
# except ZeroDivisionError:
#   - code -
# (IOError, ValueError): # denotes IOError or ValueError
#   - code -
# except:
#   - code -
# else:     # this command must follow the last (and at least one) exception catcher. The code here is executed when the try code does not encounter an error
#   - code -
# finally:
#   - code which will always be executed -
# 
# for catching the error -> except errorType as e:

while True:
    try:
        n = input("Please enter an integer: ")
        n = int(n)
    except ValueError as err:
        print(err)
        print("No valid integer! Please try again ...")
    else:
        print("Hello from the else code :D")
        break
    finally:
        print("Hello from the finally code n_n")
print("Great, you successfully entered an integer!")
print()

# raise - used to initiate a runtime error manually, or - if it is followed by no error type - push the error up in scope
# raise ValueError

def f():
    try:
        x = int("four")
    except ValueError as e:
        print("got it in the function :-) ", e)
        raise # pushing the error up in scope

try:
    f()
except ValueError as e:
    print("got it :-) ", e)
print()