# Modules are essentially regular python scripts with functions, though they can also be written in other languages and linked. 
# Modules are executed upon importing, thus allowing for settup. This step is only performed once per session, unless a reload is called (found in the importlib module)
# They can also be run on their own as a program. Accessing the global "__name__" will reveal how the file is being executed ("__main__" indicates that are being run as the main program)
# When importing; python first looks to the local folder, then the directories of 'PYTHONPATH' (if set), and finally the the standard install path (eg. /usr/lib/python3.5)

# import a module
import pickle
import pickle, math

# import a module as a namespace
import pickle as python_storage

# importing specific functions from a module
# these functions won't need a prefix
from math import pi
from math import pi, sin, cos

# importing specific functions from a module and rename
# these functions won't need a prefix
from math import pi as getPI
from math import pi as getPI, sin as math_sin



# reveal the location of the module
# this function does not work on linked C libraries
print( math.__file__ )
print()

# discover the valid attributes and methods for a module
print( dir(math) )
print()