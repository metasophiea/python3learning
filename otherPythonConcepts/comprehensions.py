# this is a method of producing lists
# this method removes the need for lambdas, map(), filter() and reduce() (or at least should)


# list comprehensions - this returns a list
# [ outputFormat logic ]
# multiplying a list's contents by 2
aList = [1,2,3,4]
print( [ x*2 for x in aList ] )
print()
# multiple outputs - this produces a list of tuples
aList = [1,2,3,4]
print( [ (x,x,x) for x in aList ] )
print()
#   with more complex logic
print( [ (x,y,z) for x in range(0,2) for y in range(0,2) for z in range(0,2)] )
print( [ (x,y,z) for x in range(0,2) for y in range(0,2) for z in range(0,2) if x==y ] )
print()
notPrimes = [j for i in range(2, 8) for j in range(i*2, 100, i)] # list of numbers from 2 to 100 that are producible with multiplication (lots of multiple values)
print( [x for x in range(2, 100) if x not in notPrimes] ) #primes from 2 to 100
print()
#   double list input
listA = ["square","circle","triangle"]
listB = ["red","green","blue"]
print( [ (x,y) for x in listA for y in listB ] ) #produces all possible combinations of these two lists
print()


# generator comprehensions - this returns a generator
# ( outputFormat logic )
print(list(     ((x*2) for x in range(1,5))     ))
print()

# set comprehensions - this returns a set
# { outputFormat logic }
print( {(x*2) for x in range(1,5)} )
print()
# a more efficient version of the prime finder from above
notPrimes = {j for i in range(2, 8) for j in range(i*2, 100, i)} # list of numbers from 2 to 100 that are producible with multiplication (no multiple values)
print( {x for x in range(2, 100) if x not in notPrimes} ) #primes from 2 to 100
print()


# variables edited in the logic of the comprehension are local to it's scope
x = "hello"
print( [ (x,y) for y in range(9) ] )
print()
