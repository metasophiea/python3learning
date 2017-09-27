# a hash map

a = {}
a = {"key":"value", "key2":2, "key4":7654}
a["key3"] = [1,2,3]
print(a)
print()

# similar to lists, copying dictionaries  doesn't duplicate the inner data, for that one must deep copy
# (there's some deepcopy() function in the 'copy' module)
# interestingly, the memory conservation from the variables file remains 

print("- retrieval")
print("\treturns the value associated with this key")
print( a["key"] )
print()

print("- unpack")
print("\ta single asterisk unpacks a dictionary into a comma-separated 'list' of the keywords for use with a function")
print("\tdouble asterisk unpacks into a comma-separated keyword 'list' for use with a function")
print( a )
print( *a, sep="-" )
def func(key,key2,key4,key3):
    print(key)
    print(key2)
    print(key3)
    print(key4)
func( **a )
print()

print("- get")
print("\treturns the value associated with this key. If no value is found \"none\" is returned")
print( a.get("key") )
print()

print("- items")
print("\treturns list of tuples of all the dictionaries data")
print( a.items() )
print()

print("- keys")
print("\treturns list of the keys")
print( a.keys() )
print()

print("- values")
print("\treturns list of the values")
print( a.values() )
print()

print("- update")
print("\tappends/updates a dictionary")
a.update( {"key":"newValue", "key7":200} )
print(a)
print()

print("- del")
print("\tdeletes the entry with this key")
del a["key3"]
print(a)
print()

print("- pop")
print("\tpops element from front of dictionary, returning that element's value")
print( a.pop("key","defaulted value to return if key isn't found") )
print( a.pop("key","defaulted value to return if key isn't found") )
print(a)
print()

print("- popitem")
print("\tpops an element from the dictionary")
print( a.popitem() )
print(a)
print()

# in
# this tests if an item exists within a dictionary
print( "key" in a )
print( "key2" in a )
print()