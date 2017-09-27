# this is a method of wrapping a function in code with another function
# enabled by python's ability to return functions as objects

print("- simple decoration")
def example_decorator(function):

    def function_wrapper(x):
        print("Before calling " + function.__name__)
        function(x)
        print("After calling " + function.__name__)

    return function_wrapper

def function(var):
    """a simple function"""
    print("welcome to function")
    print( var + 1 )



function(1)
print()

# applying decoration
function = example_decorator(function)
function(10)
print()
print()








print("- decoration streamlined")
# this application of decoration can be streamlined with the @ symbol:
@example_decorator
def function2(var):
    print("welcome to function2")
    print( var + 2 )

function2(100)
print()








print("- decorating with a static value")
# a decorator can also contain static values:
def example_decorator_withStaticValues(function):

    def function_wrapper(x):
        function_wrapper.count += 1
        print("Before calling " + function.__name__)
        function(x)
        print("After calling " + function.__name__)
        print("this was call number: " + str(function_wrapper.count))

    function_wrapper.count = 0

    return function_wrapper

@example_decorator_withStaticValues
def function3(var):
    print("welcome to function3")
    print( var + 3 )

function3(100)
function3(200)
function3(300)
print()








print("- decorating with a parameters value")
# here we see how one can add a parameter to the decorator during decoration of the function itself
def example_decorator_withParametersValue(parameter):
    def decorator(function):
        def function_wrapper(x):
            print("Before calling " + function.__name__)
            print("parameter: " + parameter )
            function(x)
            print("After calling " + function.__name__)
        return function_wrapper
    return decorator

@example_decorator_withParametersValue("this is where the parameter goes")
def function4(var):
    print("welcome to function4")
    print( var + 4 )

# alternate Method
# function4 = example_decorator_withParametersValue("this is where the parameter goes")(function4)

function4(100)
print()








print("- dealing with metadata")
# decorating a function replaces its metadata with the data of the return function
print( function.__name__ ) # >> function_wrapper
print( function.__doc__ ) # >> None
print( function.__module__ ) # >> __main__
print()
# so, one can compensate:

def example_decorator2(function):
    def function_wrapper(x):
        print("Before calling " + function.__name__)
        function(x)
        print("After calling " + function.__name__)

    function_wrapper.__name__   = function.__name__
    function_wrapper.__doc__    = function.__doc__
    function_wrapper.__module__ = function.__module__

    return function_wrapper

@example_decorator2
def function5(var):
    """a simple function"""
    print("welcome to function")
    print( var + 5 )

print( function5.__name__ ) # >> function5
print( function5.__doc__ ) # >> a simple function
print( function5.__module__ ) # >> __main__
print()

# or we can make things easier with the "wraps" function from the "functools" module, which covers things for us
from functools import wraps

def example_decorator3(function):
    @wraps(function)
    def function_wrapper(x):
        print("Before calling " + function.__name__)
        function(x)
        print("After calling " + function.__name__)

    return function_wrapper

@example_decorator3
def function6(var):
    """a simple function"""
    print("welcome to function")
    print( var + 6 )

print( function6.__name__ ) # >> function6
print( function6.__doc__ ) # >> a simple function
print( function6.__module__ ) # >> __main__
print()








# One can also decorate the definition of a class
def someFunction(self, *args):              
    return "The value a is " + str(self.a)

def classDecorator(cls):  
    cls.method = someFunction
    return cls

@classDecorator
class classToBeDecorated: 
    a = 10

a = classToBeDecorated()
print( a.method() )
print()
# in this way, one is able to decide whether a class should have a method at runtime (or whenever)