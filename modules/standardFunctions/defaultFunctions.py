# open
print("- open")
print("\topens a file and returns a link to said file")
file_ = open("data.txt","w")
print("42 is the answer, but what is the question?", file=file_)
file_.close()
print()

# zip
print("- zip")
print("\ttakes multiple lists and produces an iterator of tuples, matching the lists together")
print("\tthis iterator can be made into a list, or a dictionary")
zipList = zip( ["item_1", "item_2", "item_3", "item_4", "ignored item"], ["1_item", "2_item", "3_item", "4_item"],[1,2,3,4])
print( zipList )
print( list(zipList) )
print( dict( zip( ["item_1", "item_2", "item_3", "item_4"], ["1_item", "2_item", "3_item", "4_item"]) ) ) #zip remade as iterator was spent
print()

# max
# max(iterable[, key])
# max(arg1, arg2, *args[, key])
print("- max")
print("\ttakes a list or tuples and returns the element within that object with the highest value")
maximum = max( [1,2,3] )
print(maximum)
print()
# one can also find the highest value in a dictionary with this function like so
dictionary = {"key1":1,"key2":20,"key3":3}
print( max(dictionary) ) # this gets the largest key 
print( max(dictionary,key=dictionary.get) ) # this gets the key with the largest value
print()

# range
print("- range")
print("\ttakes some argument are produces an iterator of values")
print("\trange(begin,end, step)")
print(list( range(9) ))
print(list( range(0,8) ))
print(list( range(0,8,2) ))
print(list( list(range(10,-10,-1)) ))
print()

# locals
print("- locals")
print("\treturns all the local scope variables in dictionary form")
print( locals() )
print()

# dir
print("- dir")
print("\tprints the valid attributes and methods for the namespace provided")
print("if none is provided, the current local scope is used")
print( dir() )
print()

# filter(func, seq) 
# func - some input function
# seq - a sequence of objects (eg. list) upon which the func will be applied one by one. Function must return a boolean value
# this function returns an iterator or the results
# This function applies the function 'func' to each object in the sequence, if the result of that function is 'true' the object is added to the returned sequence
aList = [0,1,2,3,4,5,6,7,8,9]
noOdds  = lambda input : input%2!=0
noEvens = lambda input : input%2==0
print(list( filter(noOdds,aList) ))
print(list( filter(noEvens,aList) ))
print()

# getattr(obj, attribute, default)
# obj       - the object of interest
# attribute - the attribute in the object to access (as a string)
# default   - the value to return if the object cannot return a value for the attribute
# this function searches the object for the attribute provided (in the usual way) if none is found, the default attribute is returned
class exampleClass:
    pass

anObj = exampleClass()
anObj.newAttribute = "Hello"

print( anObj.newAttribute )
print( getattr(anObj ,"newAttribute",  "oops") )
print( getattr(anObj, "fakeAttribute", "oops") )
print()