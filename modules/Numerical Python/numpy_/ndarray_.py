import numpy

# The ndarray Object
#   Used within the numpy module as the main data type for storing items. 








print("-- Basic Creation --")
# Creation of a Zero-dimensional Array (a scalar)
x = numpy.array(42) # produces a "ndarray" object
print("x:", x)
print("The type of x: ", type(x))
print("The dimension of x:", numpy.ndim(x))
print()

# Creation of a One-dimensional Array (a vector)
cvalues = [20.1, 20.8, 21.9, 22.5, 22.7, 22.3, 21.8, 21.2, 20.9, 20.1]
C = numpy.array(cvalues)
print("C:",C)
print("The dimension of array:", numpy.ndim(C)) 
print( C*(9/5) + 32 ) # applying a mathematical operation to each of the items in an ndarray
print()

# Creation of a Multi-dimensional Array (made with the nesting of regular arrays)
A = numpy.array(
    [
        [3.4, 8.7, 9.9], 
        [1.1, -7.8, -0.7],
        [4.1, 12.3, 4.8]
    ]
)
B = numpy.array(
    [
        [ [111, 112], [121, 122] ],
        [ [211, 212], [221, 222] ],
        [ [311, 312], [321, 322] ]
    ]
)
print(A)
print("The dimension of array:", numpy.ndim(A)) 
print()
print(B)
print("The dimension of array:", numpy.ndim(B)) 
print()

# Creation of arrays of a given number
print( numpy.ones((2,3)) ) # the 'ones' function takes a tuple of the desired dimensions
print( numpy.ones((3,4),dtype=int) ) # by default, the number will be of type float; thus 
                                     # one must set the optional parameter 'dtype' to int
print( numpy.zeros((2,4)) )
# Creating an array of a given number, with the same shape as a different array
print( numpy.ones_like(A) )
print( numpy.zeros_like(A) )








print("\n\n\n\n-- The Shape Of An Array --")
#   the 'shape' function returns a tuple of numbers representing the length of dimensions of the array
# The order is which the numbers are listed indicates the order in which the indices are processed.
x = numpy.array(
    [ 
        [67, 63, 87],
        [77, 69, 59],
        [85, 87, 99],
        [79, 72, 71],
        [63, 89, 93],
        [68, 92, 78]
    ]
)
print(x)
print("The dimension of array:", numpy.ndim(x)) 
print(numpy.shape(x)) # = x.shape
print()

# one can also adjust the shape of the array (so long as the total number of items remains the same)
x.shape = (3, 6)
print(x)
x.shape = (9, 2)
print(x)
x.shape = (1, 18)
print(x)
print()

# further examples
x = numpy.array(11)
print(numpy.shape(x))
print()

B = numpy.array(
    [ 
        [[111, 112], [121, 122]],
        [[211, 212], [221, 222]],
        [[311, 312], [321, 322]] 
    ]
)
print(B.shape)
print()







print("\n\n\n\n-- Indexing And Slicing --")
# standard indexing (the same as regular python)
single = numpy.array([1, 1, 2, 3, 5, 8, 13, 21])
double = numpy.array([[11,12,13,14,15],[21,22,23,24,25],[31,32,33,34,35],[41,42,43,44,45],[51,52,53,54,55]])
triple = numpy.array([[[111, 112], [121, 122]],[[211, 212], [221, 222]],[[311, 312], [321, 322]]])
print(single[0])
print(single[-1])
print(double[1][0])
print(triple[0][1][0])
print()

# more efficient indexing
print(single[0])
print(single[-1])
print(double[1,0])
print(triple[0,1,0])
# the output is the same, but this stops intermidiate arrays being created, stored and subsequently accessed
print()

# slicing (the same as regular python)
print("- single slicing")
print(single[2:5])
print(single[:4])
print(single[6:])
print(single[:])
# multidimensional slicing can be done with standard indexing, but we're going to use the more efficient method from here out
print("- double slicing")
print(double[:3,2:])
print(double[3:,:])
print(double[::2,4:]) # even stepping is possible
# Note: unlike standard arrays; slicing numpy arrays does not produce a new array, but a view of the original object.
#       As such; any modification made to a view will effect the original array.








print("\n\n\n\n-- Copying --")
# numpy.copy(obj, order='K')
# obj	    the array to copy
# order	    The possible values are {'C', 'F', 'A', 'K'}. This parameter controls the memory layout of the copy. 
#           'C' - C-order (default)
#           'F' - Fortran-order
#           'A' - 'F' if the object 'obj' is Fortran contiguous, 'C' otherwise
#           'K' - match the layout of 'obj' as closely as possible.
x = numpy.array([[42,22,12],[44,53,66]], order='F')
y = x.copy()
x[0,0] = 1001
print(x)
print(y)
print(x.flags['C_CONTIGUOUS'])
print(y.flags['C_CONTIGUOUS'])
print()

# there is also a copy commaned in the ndarray method list (with the same 'order' parameter available)
x = numpy.array([[42,22,12],[44,53,66]], order='F')
y = x.copy()
x[0,0] = 1001
print(x)
print(y)
print(x.flags['C_CONTIGUOUS'])
print(y.flags['C_CONTIGUOUS'])








print("\n\n\n\n-- Identity Array --")
# there are two functions that create identity arrays
# the first function creates standard identity arrays in the usual way, the second function
# allows one you create non-square arrays, with the diagonal of 1's offset to a selected degree

# numpy.identity(n, dtype=None)
# n	        An integer number defining the number of rows and columns of the output, i.e. 'n' x 'n'
# dtype	    An optional argument, defining the data-type of the output (default is 'float')
print( numpy.identity(4) )
print( numpy.identity(4, dtype=int) )

# numpy.eye(N, M=None, k=0, dtype=float)
# N	        An integer number defining the rows of the output array
# M	        An optional integer for setting the number of columns in the output. 
#            If it is None, it defaults to 'N'
# k	        Defining the position of the diagonal. The default is 0. 0 refers to 
#            the main diagonal. A positive value refers to an upper diagonal, and 
#            a negative value to a lower diagonal
# dtype	    Optional data-type of the returned arra
print( numpy.eye(5, 8, k=-1, dtype=int) )
print( numpy.eye(5, 8, k=0, dtype=int) )
print( numpy.eye(5, 8, k=1, dtype=int) )
print()








print("\n\n\n\n-- Numerical And Logical Operations --")
# Scalars
# this form of operation is much much faster than equivalent actions in raw python (with a for-loop or comprehension) 
vector = numpy.array( [2,3, 7.9, 3.3, 6.9, 0.11, 10.3, 12.9] )
print(vector)
print(vector + 2)
print(vector - 2)
print(vector * 2)
print(vector ** 2)
print(vector / 2)
print(vector // 2) # divide with floor
print()

# Vectors
# - Component-wise Operations
A = numpy.array(
    [ 
        [11, 12, 13], 
        [21, 22, 23], 
        [31, 32, 33] 
    ]
)
B = numpy.ones( (3,3) )
print(A + B)
print(A - B)
print(A * B)
print(A / B)
print()
# - Matrix-wise Operations
print( numpy.dot(A,B) ) # dot product (one can also write "A.dot(B)")
print()

# Comparison
# standard comparison will return an vector of equal dimension, but with the boolean result of checking each value
A = numpy.array([ [11, 12, 13], [21, 22, 23], [31, 32, 33] ])
B = numpy.array([ [11, 12, 13], [21, 22, 23], [31, 32, 33] ])
C = numpy.array([ [11, 102, 13], [201, 22, 203], [31, 32, 303] ])
print( A == C )
print( A > C )
# complete comparison can be performed with the 'numpu.array_equal' command
# this will only return true when the arrays are exactly the same (in value)
print( numpy.array_equal(A,B) )
print( numpy.array_equal(A,C) )
print()

# Logical
# these operations can be performed on vectors which consist solely of boolean values
a = numpy.array([ [True, True], [False, False]])
b = numpy.array([ [True, False], [True, False]])
print( numpy.logical_or(a, b)  )
print( numpy.logical_and(a, b) )
print()



