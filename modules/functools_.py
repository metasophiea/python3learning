import functools

# @wraps(function)
# used in decorators to wrap decorated functions in the correct metadata

# reduce(func, seq) 
# func - some input function
# seq - a sequence of objects (eg. list) upon which the func will be applied two by two
# this function returns a single object from the sequence provided
#   This function passes over the provided sequence in twos to produce a single result. 
# First the first two objects are passed to the function 'func' from which a single 
# results returns. This result is then passed back into 'func' with the third object 
# from the sequence. Then the result of this is passed into 'func' with the fourth object
# and so on, until only one object remains.
# Diagram:
#   list = [1,2,3,4]
#   func is a + b
#   reduce -> func(func(func(1,2),3),4)
aList = (1,2,3,4)
func = lambda a,b : a+b
print( functools.reduce(func,aList) )
print()
# reduce - get max
aList = (1,2,3,4)
func = lambda a,b : a if (a > b) else b
print( functools.reduce(func,aList) )
print()
# reduce - factorial
aList = (1,2,3,4)
func = lambda a,b : a*b
print( functools.reduce(func,aList) )
print()