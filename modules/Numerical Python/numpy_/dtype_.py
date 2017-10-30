import numpy

# The dtype Object
#   Used within the numpy module with ndarrays, so allow for multiple data 
# types to be stored in an array. It's alot like a 'structure' from C, and
# seems to be for table-like data to be stored (like a spreadsheet or database)
# though one is unable to use them on their own.

# Basic usage
num = numpy.dtype(int)
lst = [ [3.4, 8.7, 9.9], 
        [1.1, -7.8, -0.7],
        [4.1, 12.3, 4.8] ]
A = numpy.array(lst, dtype=num)
print(A)
print()

# dtype constructors take a data type, here are a few of the possiblities
print( numpy.dtype( int ) )
print( numpy.dtype( str ) )
print( numpy.dtype( float ) )
print()
print( numpy.dtype( numpy.int   ) ) # system default
print( numpy.dtype( numpy.int8  ) )
print( numpy.dtype( numpy.int16 ) )
print( numpy.dtype( numpy.int32 ) )
print( numpy.dtype( numpy.int64 ) )
print()
# it is easier however (and somewhat more useful) to use the string-based entry
print( numpy.dtype('i') ) 
print( numpy.dtype('f') ) 
print( numpy.dtype('d') )
print( numpy.dtype('S') ) 
print()
# a number represents the number of bytes to be used
print( numpy.dtype('i1') ) # i1 - i8
print( numpy.dtype('f2') ) # # f2 - f16 ('f1' doesn't seem to be allowed)
                           # ('d' seems to be a fixed type (probably because it's "double float"))
print( numpy.dtype('S1') ) # S0 - ?
print()
# '>' and '<' are used to define bit order ('little-endian' and 'big-endian' respectively)(default is system order)
print(numpy.dtype('>i2').byteorder)
print(numpy.dtype('i2').byteorder) # the '=' symbol means that the bit order is the same as the system default
print(numpy.dtype('<i2').byteorder) 
print("\n\n")








# Records
#   One can create a non-homogenous collection of data within a dtype, by defining 
# the name of each section along with it's data type in a tuple (which in turn can be
# placed in a homogenous list (of this data type (dtype (very clever))))
num = numpy.dtype(
    # ("columnName","columnDataType")
    [ ("a","i2"), ("b","i2") ]
)
print(num)
# placing this type into an array:
array = numpy.array(
    [
        (10, 20),
        (100, 200)
    ],
    dtype = num
)
print(array) # getting the whole array
print(array["a"]) # getting just the 'a' records
print(array["a"][0]) # getting more specific
print()
# Multi Level Records
description = numpy.dtype(
    [
        ("sub1", numpy.dtype([ ("a","i2"),("b","i2") ])),
        ("sub2", numpy.dtype([ ("a","i2"),("b","i2") ])) 
    ]
)
array = numpy.array(
    [
        ((10, 20),(100, 200)),
        ((10, 20),(100, 200))
    ],
    dtype = description
)
print(array) # getting the whole array
print(array["sub1"]) # getting just the 'sub1' records
print(array["sub1"]["a"]) # getting just the 'sub1:a' records
print(array["sub1"]["a"][0]) # getting more specific