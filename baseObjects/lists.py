a = []
a = [1,2,3]
print(a)
print()

# similar to JS, copying lists doesn't duplicate the inner data, for that one must deep copy
# (there's some deepcopy() function in the 'copy' module)
# interestingly, the memory conservation from the variables file remains 

print("- [] = index")
print("\tgets element from list")
print( a[0] )
print()

print("- * = unpack")
print("\tunpacks a list into a comma-separated 'list' for use with a function")
alist = [1,2,3,4]
print( alist, sep="-")
print( *alist, sep="-")
print()

print("- len")
print("\tgets list length")
print( len(a) )
print()

print("- in")
print("\tis the element in the list")
print( 1 in a )
print()

print("- pop")
print("\tpops element from front of list, returning that element")
print( a.pop() )
print(a)
print()

print("- append")
print("\tadds element to the end of a list")
print("\t(one can also write: a = a + element)")
a.append(2)
print(a)
print()

print("- insert")
print("\tplaces element in list at index")
a.insert(0,100)
print(a)
print()

print("- remove")
print("\tremoves first element matching argument")
a.remove(2)
print(a)
print()

print("- extend")
print("\tadds argument element to the end of root")
print("\t(one can also write: a = a + b)")
a.extend( [6,7,8] )
print(a)
print()

print("- index")
print("\tgets index of the first occurrence of the argument")
print( a.index(6) )
print()

print("- sort")
print("\tsorts list")
a.sort()
print(a)
print()

print("- reverse")
print("\treverses list")
a.reverse()
print(a)

print("- multi dimensional lists")
a = [["strings","Hello"],[1,2,3],[4,5,6]]
print(a)
print()