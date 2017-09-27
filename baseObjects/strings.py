string = "Hello"
multiLineString = '''
    You can type anything here "" '' """
(except triple quote of course)'''
concatString = string + string
multString = string * 3
toString = str(100+1)

print(string)
print(multiLineString)
print(toString)
print(concatString)
print(multString)
print()

print("- [] = index")
print("     gets character from string")
a = "Hello"
print("a[0] -> \"H\"")
print( a[0] )
print("a[1] -> \"e\"")
print( a[1] )
print("a[-1] -> \"o\"")
print( a[-1] )
print("a[:] -> \"Hello\"")
print( a[:] )
print("a[1:] -> \"ello\"")
print( a[1:] )
print("a[:3] -> \"Hel\"")
print( a[:3] )
print("a[1:3] -> \"el\"")
print( a[1:3] )
print("a[::2] -> \"Hlo\"")
print( a[::2] )
print("a[::-1] -> \"elloH\"")
print( a[::-1] )
print()

print("- len")
print("\tgets string length")
print( len(a) )
print()

print("- index")
print("\tgets index of the first occurrence of the argument")
print( a.index("H") )
print()

print("- count")
print("\tcounts up the number of occurrences of the argument")
print( a.count("H") )
print()

print("- lower")
print("\tsets all characters to their lower case")
print( a.lower() )
print()

print("- upper")
print("\tsets all characters to their upper case")
print( a.upper() )
print()

print("- split") # str.split([sep[, maxsplit]]) 
print("\tsplits up string on matching argument (space by default)")
print( a.split("e") )
print( "A big long and very important string".split(None,4) ) #maxsplit stops the splitting operation after a certian number of splits
print()

print("- join(list)")
print("\tthe reverse of split")
print( "".join(["1","2","3"]) )
print()

print("- find")
print("\tgets index of text that matches argument")
print( a.find("ll") )
print()

print("- startswith")
print("\treturns True is string starts with argument")
print( a.startswith("E") )
print()

print("- endswith")
print("\treturns True is string ends with argument")
print( a.endswith("o") )
print()

print("- center")
print("\tcenters in provided string into a string of the provided length or larger, using the provided character as padding (space by default)")
print( a.center(10,"-") )
print()

print("- ljust")
print("\tleft justifies the provided string into a string of the provided length or larger, using the provided character as padding (space by default)")
print( a.ljust(10,"-") )
print()

print("- rjust")
print("\tright justifies the provided string into a string of the provided length or larger, using the provided character as padding (space by default)")
print( a.rjust(10,"-") )
print()

print("- zfill")
print("\tleft justifies the provided string into a string of the provided length or larger, using the character '0' as padding")
print( a.zfill(10) )
print()

print("- rstrip and lstrip")
print("\tstrips away all blank spaces to the right or left (including newlines)")
newString = "    Bonk      "
print(newString)
print(newString.rstrip())
print(newString.lstrip())
print()

# str.replace(old, new[, max]) 
# old - old string
# new - replacement string 
# max - maximum number of strings to be replaced
print("- replace")
print("\treplaces characters that match a string with the provided replacement string")
newString = "Look at all these letters!"
newString = newString.replace("es","os")
print(newString)
print()