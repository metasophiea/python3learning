# Here we have a module called "basic.py" with two simple functions

def adder(a,b):
    return a + b

def multer(a,b):
    return a * b

#   The trick with unit testing in python; is to run the modules on their own to 
# activate the tests. To do this, one looks to the '__name__' global attribute.
# print(__name__)
# This will have the string "basic.py" if this module is being imported
# or the string "__main__" if it is being run as the main file. Using this fact; all
# the function tests can be wrapped inside a if statement that tests for this string.

if __name__ == "__main__":
    print("Running unit tests")
    print("- adder")
    if( adder(1,1) == 2 ):
        print("-> successful")
    else:
        print("-> failed")
         
    print("- multer")
    if( multer(2,2) == 4 ):
        print("-> successful")
    else:
        print("-> failed")