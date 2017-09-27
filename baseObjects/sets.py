# Sets contains an unordered collection of unique and uneditable objects,
# though the sets themselves can be edited
# Frozensets are exactly the same, except they are uneditable

set_1 = set("Hello")
set_2 = set( ["JavaScript", "Python", "C++"] )
set_3 = set(("Paris", "Lyon", "London","Berlin","Paris","Birmingham"))
set_4 = {1,2,3,4}
frozenSet_1 = frozenset(["Dublin","Cork","Galway"])
# one cannot use a list as an element (as those are editable)

print(set_1)
print(set_2)
print(set_3)
print(set_4)
print(frozenSet_1)
print()

print("- add")
print("\tadds and element to the set")
set_2.add("Java")
print(set_2)
print()

print("- clear()")
print("\tempties the set")
set_1.clear()
print(set_1)
print()

print("- copy")
print("\tcreates a shallow copy")
set_5 = set_2.copy()
set_5.clear()
print(set_2)
print(set_5)
print()

print("- difference")
print("\treturns the elements that are in the root set, that aren't in the argument set")
diffSet_1 = {1,2,3,4,5}
diffSet_2 = {1,2,3,4,6}
print(diffSet_1.difference(diffSet_2))
print()

print("- difference_update")
print("\tremoves from the root set, elements that appear in the argument set")
diffSet_1.difference_update(diffSet_2)
print(diffSet_1)
print(diffSet_2)
diffSet_1 = {1,2,3,4,5}
diffSet_1 = diffSet_1 - diffSet_2
print(diffSet_1)
print(diffSet_2)
print()

print("- discard")
print("\tremoves the element from the set (if it is there)")
discardSet = {1,2,3,4}
discardSet.discard(1)
discardSet.discard(5)
print(discardSet)
print()

print("- remove")
print("\tremoves the element from the set - if it is there - or throws a 'KeyError' if it's not to be found")
discardSet = {1,2,3,4}
discardSet.remove(1)
# discardSet.remove(5)
print(discardSet)
print()

print("- union")
print("\treturns the union of the two sets")
unionSet_1 = {1,2,3,4}
unionSet_2 = {3,4,5,6}
unionSet_3 = unionSet_1.union(unionSet_2)
print(unionSet_3)
unionSet_1 = {1,2,3,4}
unionSet_2 = {3,4,5,6}
unionSet_3 = unionSet_1 | unionSet_2
print(unionSet_3)
print()

print("- intersection")
print("\treturns the elements that appear in both sets")
intersectionset_1 = {1,2,3,4}
intersectionset_2 = {3,4,5,6}
intersectionset_3 = intersectionset_1.intersection(intersectionset_2)
print(intersectionset_3)
intersectionset_1 = {1,2,3,4}
intersectionset_2 = {3,4,5,6}
intersectionset_3 = intersectionset_1 &intersectionset_2
print(intersectionset_3)
print()

print("- isdisjoint")
print("\treturns true if there are no common elements between sets")
isdisjointSet_1 = {1,2}
isdisjointSet_2 = {2,3}
isdisjointSet_3 = {8,9}
print( isdisjointSet_1.isdisjoint(isdisjointSet_2) )
print( isdisjointSet_1.isdisjoint(isdisjointSet_3) )
print()

print("- issubset")
print("\treturns true if the argument set contains all the elements the root set does")
issubsetSet_1 = {1,2,3,4}
issubsetSet_2 = {1,2}
print( issubsetSet_2.issubset(issubsetSet_1) )
print( issubsetSet_1 < issubsetSet_2 )
print( issubsetSet_2 < issubsetSet_1 )
print()

print("- issuperset")
print("\treturns true if the root set contains all the elements the argument set does")
issupersetSet_1 = {1,2,3,4}
issupersetSet_2 = {1,2}
print( issupersetSet_1.issuperset(issupersetSet_2) )
print( issupersetSet_1 > issupersetSet_2 )
print( issupersetSet_2 > issupersetSet_1 )
print()
print()

print("- pop")
print("\tremoves and returns a random element")
print(set_2)
print( set_2.pop() )
print(set_2)
print()