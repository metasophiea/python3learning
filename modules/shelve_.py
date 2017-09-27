# similar to the pickle module, this module is used to store data in files. However, here stored data can be accessed directly, thus removing the need to load/save the data (though the shelve itself needs to be closed)
# key's must be strings. One can cast a shelve object into a normal object.
# it seems sub-data in an object in a shelve cannot be edited, only top level...
import shelve

import os
filepath = os.path.dirname(__file__)

# writing to a shelve
phoneBook = shelve.open(filepath+"/aShelve")

phoneBook["bwalsh"] = {"name":"Brandon Walsh", "number":"8888"}
phoneBook["cfandango"] = {"name":"Clem Fandango", "number":"1234"}

phoneBook.close()



# reading from and editing a shelve
phoneBook = shelve.open(filepath+"/aShelve")

print( phoneBook["bwalsh"] )
phoneBook["cfandango"] = {"name":"Clem Fandango", "number":"1111"}
print( phoneBook["cfandango"]["number"] )

phoneBook.close()
