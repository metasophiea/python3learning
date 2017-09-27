import doctest
#   The doctest module uses comments within functions as guides to perform tests. These
# test texts are based on the interactive session functionality of python (hence the >>>)
# To make a test, one simply writes >>> followed by the function and arguments to be 
# tested. The next line contains te expected output. If everything goes well; everything
# will be quiet. If not, failure logs will be produced in the console.
#   One must run the function doctest.testmod() using the same method of testing the 
# __name__ global as with basic testing.

def adder(a,b):
    # The first test will work, but the second will fail. This will not stop execution however
    """
    >>> adder(1,2)
    3
    >>> adder(1,2)
    2
    >>> adder(0,2)
    2
    """

    return a + b


if __name__ == "__main__":
    doctest.testmod()