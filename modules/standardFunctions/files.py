# how to get the filepath of the folder containing the script
import os
filepath = os.path.dirname(os.path.realpath(__file__))

# open a file (for reading by default)
file_obj = open(filepath+"/testFile.txt")

# printing each line of the file
print("- reading a file -")
for line in file_obj:
    print( line )
    # the line includes a newline, if one exists in the file

# close a file
file_obj.close()
print()


# open a file for writing
file_obj = open(filepath+"/testFile.txt","w")
file_obj.write("A very many important things are written here.")
file_obj.close()


# open a file for appending
file_obj = open(filepath+"/testFile.txt","a")
file_obj.write("\nYou would do well to remember them for important situations")
file_obj.close()


# open a file for reading and writing
file_obj = open(filepath+"/testFile.txt","w+")
file_obj.write("A very many important things are written here.")
file_obj.close()
# open a file for reading and writing (keeping the original data)
file_obj = open(filepath+"/testFile.txt","r+")
file_obj.write("A very many important things are written here.\nYou would do well to remember them for important situations")
file_obj.close()



# the 'with' statement
# used like a "try/catch" block. Useful for not having to write the close code
print("- reading a file using the 'with' statement -")
with open(filepath+"/testFile.txt") as file_obj:
    for line in file_obj:
        print( line )
print()



# reading an entire file in one go
print("- reading a file in on go, producing a list of all the lines -")
lines = open(filepath+"/testFile.txt").readlines()
print(lines)
print()
print("- reading a file in on go, producing a string of all lines -")
lines = open(filepath+"/testFile.txt").read()
print(lines)
print()

# using the functions 'tell' and 'seak'
print("- using the functions 'tell' and 'seak' -")
file_obj = open(filepath+"/testFile.txt")
print( file_obj.tell() )
print( file_obj.read(7) )
print( file_obj.tell() )
print( file_obj.read(4) )
print("---")
print( file_obj.seek(2) )
print( file_obj.read(4) )
print("---") # combination
print( file_obj.seek( file_obj.tell()+6) )
print( file_obj.read(9) )
print()
