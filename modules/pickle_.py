# This module is used for the serialization of data
import pickle

# dump
# pickle.dump(obj, file[,protocol, *, fix_imports=True])
# setting protocol example: pickle.dump(obj, file, 3)
# protocols:
# 0 : ascii format (0.0)
# 1 : binary format (0.0)
# 2 : binary format (2.3)(more efficient pickling of new-style classes)
# 3 : binary format (3.0)(default of python3)
# setting 'fix_imports' to true makes pickle map new Python3 names to the old module names used in Python2, making the pickle data stream readable with Python 2

import os
filepath = os.path.dirname(__file__)

# pickling data
obj = ["all this crazy data",1,2,3]

file_obj = open(filepath+"/pickledStuff.pkl", "wb")
pickle.dump(obj, file_obj)
file_obj.close()

# unpickling data
file_obj = open(filepath+"/pickledStuff.pkl", "rb")
print( pickle.load(file_obj) )
file_obj.close()

# you can only pickle one object into a file, thus consolidation is a good idea if you want to use only one file