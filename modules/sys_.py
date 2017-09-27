#       The sys module provides information about constants, functions and methods of the Python
#   interpreter, allowing one to interact with both the python interpreter, and the shell around it.


import sys


# Getting the python interpreter's version number and details
print( sys.version )
# similar to above, but presented in a tuple 
#       major - minor - micro - release-level - serial
# release level can be any of: 'alpha', 'beta', 'candidate', or 'final', the rest are integers
print( sys.version_info )
print()


# A dictionary of all the modules which have been loaded. This can be edited to 
# enforce the reloading of modules
#print( sys.modules ) #its a lot to print
print()


# Getting the python interpreter's executable location
print( sys.executable )
print()


# The modules search paths, in order
print( sys.path )
print()


# Getting the machine's name
print( sys.platform )
print()


# The maximum number storable in a single byte on the current system
# note: since python3, this is not a limit
# (on mac, this is 9223372036854775807, which is 63 1's in binary)
print( sys.maxsize )
print()


# An integer giving the largest supported code point for a Unicode character
#   The value of this depends on the configuration option that specifies whether 
# Unicode characters are stored as UCS-2 or UCS-4
print( sys.maxunicode )
print()


# Discovering the python interpreter's native byte order
#   'big'    : big-endian    (most-significant byte first) 
#   'little' : little-endian (least-significant byte first)
print( sys.byteorder )
print()


# Accessing and setting the recursion limit
print( sys.getrecursionlimit() )
sys.setrecursionlimit(500)
print( sys.getrecursionlimit() )
print()


# Accessing the command-line arguments used to activate this script
# (as expected, the first argument is the address of the script itself)
print(sys.argv)
print()


# sys.displayhook is the listener the interpreter uses during interactive mode to print returned stuff 
# to the console. One can rebind this in the usual way. It's pretty useless in regular use
# def my_display(x):
#     print("out: ", x)
#
# sys.displayhook = my_display


# Standard Data Streams
#       Here one is essentially bypassing the 'print' and 'input' functions to access the
#   shells streams directly, which grants one greater control of what is done with these
#   stream. Note however that 'print' and 'input' use the standard streams already, just 
#   with some fancy code between you and them.
sys.stdout.write("Hello\n")
sys.stderr.write("Hello\n")
#val = sys.stdin.readline()
#       One can also select the stream from within the print function, overriding destination
#   selections that have been made elsewhere
print("printing to error stream", file=sys.stderr)

#       Using BASH commands, one can redirect the input and output of these streams:
#   eg. redirect output python3 sys_.py > output.txt
#   eg. redirect input  python3 sys_.py < input.txt
#   eg. both            python3 sys_.py < input.txt > output.txt
#   in these situations; the stderr stream is still directed to the console (though can be 
#   redirected if required, but that's other BASH stuff)
#
#       One can also set up redirections within a program, and reset them also.
#
save_stdout = sys.stdout        # saving the output stream
fh = open("output.txt","w")     # opening/creating the output file
sys.stdout = fh                 # assigning the output file as the new output stream destination
print("This line goes to output.txt")
sys.stdout = save_stdout        # resetting the stream
fh.close()
#
#   The error stream can be redirected in the same way