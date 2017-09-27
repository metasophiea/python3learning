# a generator is exactly like an iterator, except none of the values extracted from it are stored in it. Instead; they are generated as needed
# there are two parts to a generator: the function and the object
# function - the logic part that determins what happens when the object is used
# object - the element returned from calling the generator function
#   The function is run to produce a generator object consisting of the logic written in the generator function, which is run when an object is 
# requested from the object. The 'yield' command precedes the object that will be provided. Execution of this function now stops until another 
# object is requested, wherein execution of the function will contine from where it left off (scoped variables and all) The 'return' command 
# (with a value) signifies the end of the generators content (a 'StopIteration') Reaching the end of the function has the same effect

# simple example
def city_generator():
    yield("London")
    yield("Hamburg")
    yield("Konstanz")
    yield("Amsterdam")
    yield("Berlin")
    yield("Zurich")
    yield("Schaffhausen")
    yield("Stuttgart")

city = city_generator()
print( next(city) )
print( next(city) )
print( next(city) )
print( next(city) )
print( next(city) )
print( next(city) )
print( next(city) )
print( next(city) )
# print( next(city) ) #traceback error: StopIteration
print()

def city_generator_2(firstCity):
    yield(firstCity)
    yield("Hamburg")
    yield("Konstanz")
    yield("Amsterdam")
    yield("Berlin")
    yield("Zurich")
    yield("Schaffhausen")
    yield("Stuttgart")

city = city_generator_2("Dublin")
print( next(city) )
print( next(city) )
print( next(city) )
print( next(city) )
print( next(city) )
print( next(city) )
print( next(city) )
print( next(city) )
# print( next(city) ) #traceback error: StopIteration
print()

# infinite logical number generaion
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

f = fibonacci()
print( next(f) )
print( next(f) )
print( next(f) )
print( next(f) )
print( next(f) )
print( next(f) )
print( next(f) )
print( next(f) ) # sequence continues forever
print()


# 'raise' and 'return' in generator functions
# these can be used to raise StopIteration errors with some extra stuff attached
# raise - a little more detail in the error
def gen():
    yield 1
    raise StopIteration("Hello there")

f = gen()
print( next(f) ) # 1
    #print( next(f) )
    # Traceback (most recent call last):
    #   File "/Users/metasophiea/Code/Python/learning/Python 3/baseObjects/generator.py", line 61, in <module>
    #     print( next(f) )
    #   File "/Users/metasophiea/Code/Python/learning/Python 3/baseObjects/generator.py", line 57, in gen
    #     raise StopIteration("Hello there")
    # StopIteration: Hello there
print()
# return
def gen():
    yield 1
    return "Hello there"

f = gen()
print( next(f) ) # 1
    #print( next(f) )
    # Traceback (most recent call last):
    #   File "/Users/metasophiea/Code/Python/learning/Python 3/baseObjects/generator.py", line 76, in <module>
    #     print( next(f) )
    # StopIteration: Hello there
print()


# send Method / Coroutines
#   This is a method for sending data to a generator as it's being used. In pervious cases the generator would wait after a yield command
# had sent a object back for the next calling. It can also be used to receive an object. Here, the generator waits until something is sent
# to it; then it assigns that object to the variable on the yield command's left (as an internal scope object). One can use genObj.send(obj)
# to send an object to the generator. The 'next' command sends a 'None' to the generator.
def simple_coroutine():
    print("     coroutine has been started!")
    while True:
        x = yield 
        print("     coroutine received: ", x)
        yield x

cr = simple_coroutine()
print("-> requesting next -"); print( next(cr) )            # begins loop, gen now waiting at 'x = yield' for input.                        Yield -> None
print("-> requesting next -"); print( next(cr) )            # input is 'None', x = None, prints x, yielding and waiting at 'yield x'.       Yield -> None
print("-> sending message -"); print( next(cr) )            # loop resets, gen now waiting at 'x = yield' for input.                        Yield -> None
print("-> sending message -"); print( cr.send("Hello") )    # input is "Hello", x = 'Hello', prints x, yielding and waiting at 'yield x'.   Yield -> "Hello"
print("-> requesting next -"); print( next(cr) )            # loop resets, gen now waiting at 'x = yield' for input.                        Yield -> None
print("-> requesting next -"); print( next(cr) )            # input is 'None', x = None, prints x, yielding and waiting at 'yield x'.       Yield -> None
# double yield and the layout of the generator means that that 'send' command is placed very particularly (specifically when the gen is waiting at 'x = yield' for input)
print()
# example of simultaneous send and receive 
def sendAndReceive():
    print("sendAndReceive has been started!")
    x = None
    while True:
        print("     sendAndReceive sending: ", x)
        x = yield x
        print("     sendAndReceive received: ", x)

cr = sendAndReceive()
print("-> requesting next -"); print( next(cr) ) 
print("-> requesting next -"); print( cr.send("Hello") ) 
print("-> requesting next -"); print( cr.send("Again") ) 
print("-> requesting next -"); print( next(cr) ) 
print()


# throw() - for throwing an exception into an in-use generator
def fibonacci2():
    a, b = 0, 1
    index = 0
    while True:
        try:
            yield a
            a, b = b, a + b
            index += 1
        except Exception:
            print("index is: " + str(index))

f = fibonacci2()
print( next(f) )
print( next(f) )
print( next(f) )
print( next(f) )
#f.throw(Exception) # prints the current index (stops execution and requires manual continue)
print( next(f) )
print( next(f) )
print( next(f) )
print( next(f) ) # sequence continues forever
print()


# using a decorator to start a generator automatically
def get_ready(gen):

    def generator(*args,**kwargs):   
        g = gen(*args,**kwargs)   
        next(g)   
        return g   

    return generator

def counter(x):
    a = x
    while True:
        yield a
        a += 1

print("on it's own")
f = counter(10)
print( next(f) ) # notice how it prints 10 first
print( next(f) )
print( next(f) )
print("now with decoration")
counter = get_ready(counter)
f = counter(10)
print( next(f) ) # notice how it prints 11 first
print( next(f) )
print( next(f) )
print()


# yield from - a method of yielding the elements of an iterator or generator through request calls
# 'send' commands will be passed through to the internal iterator/generator when appropriate
def counter(x):
    a = x
    while a < x+5:
        input = yield a
        if input != None:
            print("counter got: " + str(input) + " while the counter was: " + str(a))
        a += 1

def delegator(x):
    yield from counter(x)
    a = yield "middle section"; print("delegator got: " + str(a))
    yield from counter(x*10)

f = delegator(5)
print( next(f) )            # 5
print( next(f) )            # 6
print( next(f) )            # 7
print( f.send("Hello") )    # 8  - input caught by counter
print( next(f) )            # 9  - end of first internal generator
print( next(f) )            # middle section
print( f.send("Hello") )    # 50 - input caught by delegator
print( next(f) )            # 51
print( next(f) )            # 52
print( next(f) )            # 53
print( next(f) )            # 54 - end of second internal generator
print()


# recursive generation
# this example generator produces all the n-set permutations of the letters in a given string, in a recursive fashion
def k_permutations(items, n):
    if n==0: 
        yield []
    else:
        for item in items:
            for kp in k_permutations(items, n-1):
                if item not in kp:
                    yield [item] + kp

for kp in k_permutations("abcd", 2):
    print(kp)
print()


# generatin' generators
def generatorGenerator():
    def fibonacci():
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b
    while True:
        yield fibonacci()

f = generatorGenerator()
f_1 = next(f)
print( next(f_1) )
print( next(f_1) )
print( next(f_1) )
print( next(f_1) )
print( next(f_1) )
print( next(f_1) )
print( next(f_1) )
print( next(f_1) )
f_2 = next(f)
print( next(f_2) )
print( next(f_2) )
print( next(f_2) )
print( next(f_2) )
print( next(f_2) )
print( next(f_2) )
print( next(f_2) )
print( next(f_2) )