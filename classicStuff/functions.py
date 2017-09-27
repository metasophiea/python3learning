# def function-name(Parameter list):
#     function body

# basic example
def fahrenheit(T_in_celsius): # returns the temperature in degrees Fahrenheit
    return (T_in_celsius * 9 / 5) + 32

print("- default arguments")
def functionWithDefault( value=10 ):
    return value * 4

print( functionWithDefault() )
print( functionWithDefault(1) )
print()


print("- doc strings")
def functionWithDocString():
    """-- functionWithDocString --
this text is the doc string 
it also includes this text"""
    return 10

print( functionWithDocString.__doc__ )
print()


print("- keyword parameters")
def functionWithKeywords(a,b,c,d):
    return a - b + c - d

print( functionWithKeywords(1,d=2,c=3,b=4) )
# note that one cannot follow a keyword argument with a position based argument
# also one must be careful to not assign multiple values to the same argument
print()


print("- returning multiple values")
def functionReturningMultipleValues():
    a = 1
    b = 2
    return (a,b)

(x,y) = functionReturningMultipleValues()
print( x )
print( y )
print()


print("- global scoping a variable")
# here a global is being created. Global variables can be accessed anywhere after being created
def functionWithAGlobalVariable():
    global var
    var = 100

functionWithAGlobalVariable()
print(var)
print()
# in nesting, if this global value exists in the parent scope; the global is created and used, but the parent cannot access it
def parentScope():
    var = 10
    print(var)
    functionWithAGlobalVariable()
    print(var)

var = 0
print(var)
parentScope()
print(var)
print()


print("- nonlocal variable")
# this is like the 'global' decalration, but here you're saying "please use the variable of my parents scope"
# as you can see, the function that uses this nonlocal value must be decalred within the parent function, and after the variable itself is declared
# beyond that; normal rules apply
def parentScope_nonLocal():
    var2 = 20
    def functionWithANonLocalVariable():
        nonlocal var2
        var2 = 200

    print(var2)
    functionWithANonLocalVariable()
    print(var2)

var2 = 0
print(var2)
parentScope_nonLocal()
print(var2)
print()


print("- arbitrary arguments length")
def arithmetic_mean(first, *values):
    """ This function calculates the arithmetic mean of a non-empty
        arbitrary number of numerical values """
    return (first + sum(values)) / (1 + len(values))

# asterisk is used to denote a "tuple reference". The type of the argument received ("values") is a tuple
# useful for unknown argument length usage
print(arithmetic_mean(45,32,89,78))
print(arithmetic_mean(1,2,3,4,5,6,7,8,9))
print(arithmetic_mean(8989.8,78787.78,3453,78778.73))
print(arithmetic_mean(45,32))
print(arithmetic_mean(45))
print()


print("- arbitrary keyworded arguments length")
def f( **data ):
    print(data)

f( keyworkd_1="Hello", otherKeyword=100 )
print()


print("- static values")
# this is done by accessing the function by name within the body of the function, and setting a dynamic attribute
def functionWithStatic():
    functionWithStatic.counter = getattr(functionWithStatic, "counter", 0) + 1 
    return functionWithStatic.counter

for i in range(10):
    print( functionWithStatic() )
    
# the static value can be accessed pubically
print(functionWithStatic.counter)