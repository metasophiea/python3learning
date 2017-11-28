import numpy

# The ndarray Object
#   Used within the numpy module as the main data type for storing items. 

# Basic Creation
# The Shape Of An Array
# Indexing And Slicing
# Copying
# Identity Array
# Numerical And Logical Operations
# Editing An Array's Shape
# Matrixes








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
print()

# Masking
# one can select the elements of one vector based on a boolean array, this array can also
# be produced on the fly by judging another vector
A = numpy.array([1, 1, 2, 3, 5, 8, 13, 21])
mask = numpy.array([True, False, True, False, True, False, True, False])
print( A[ mask ] ) # this produces a completely new array
print()
# on the fly
mask = numpy.array([5, 6, 1 ,0, 8, 0, 10, 11])
print( A[mask>3] )
print()

# Integer Array Indexing
# this is a method of creating an array out of another, by selecting which elements of the first array
# you want. Multiples can be selected
A = numpy.array([1, 1, 2, 3, 5, 8, 13, 21])
selection = [1, 1, 0, 7]
print( A[selection] )
print()

# Finding non-zero values
# the 'nonzero' method (array.nonzero()) (or the 'nonzero' function (numpy.nonzero())) can be used
# to find all the non-zero values in a vector. The command returns a number of arrays - one per 
# for each dimension of the original vector - indicating the location of these values.
a = numpy.array([0, 2, 3, 0, 1])
print(a.nonzero()) # -> [1, 2, 4]
a = numpy.array([[0, 2, 3, 0, 0], [5, 0, 0, 1, 0]])
print(a.nonzero()) # -> [0, 0, 1, 1], [1, 2, 0, 3] | [xValues][yValues]
# one can then use the 'transpose' command to rearrange this data into a list of grouped locations
print(numpy.transpose(a.nonzero())) # -> [[0 1] [0 2] [1 0] [1 3]]
# it is then possible to retrieve the original values 
print( a[a.nonzero()] )








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

# Scalar Product
x = numpy.array([1,2,3])
y = numpy.array([-7,8,9])
def scalarProduct_calculationOfTheAngleBetweenTwoVectors(x, y):
    # angle = invCOS( (X•Y)/(Xmagnitude*Ymagnitude) )
    return numpy.arccos(
        numpy.dot(x,y) / (
            numpy.sqrt((x*x).sum())*
            numpy.sqrt((y*y).sum())
        )
    )

print( scalarProduct_calculationOfTheAngleBetweenTwoVectors(x, y))
print()

# Comparison
# standard comparison will return an vector of equal dimension, but with the boolean result of checking each value
A = numpy.array([ [11, 12, 13], [21, 22, 23], [31, 32, 33] ])
B = numpy.array([ [11, 12, 13], [21, 22, 23], [31, 32, 33] ])
C = numpy.array([ [11, 102, 13], [201, 22, 203], [31, 32, 303] ])
print( A == 11 ) # vector against scaler
print( A == C )  # vector against vector
print( A > C )
# one can convert these results back to a numerical value also
print( (A==C).astype(numpy.int) )
# complete comparison can be performed with the 'numpy.array_equal' command
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

# Broadcasting
# this is the process of performing arithmetic operations on matrixes of different shapes (though, only matrixes which
# are logically relatable)
A = numpy.array([ [11, 12, 13], [21, 22, 23], [31, 32, 33] ])
B = numpy.array([1, 2, 3])
print(A * B)
print(A + B)
print()
# here; the smaller matrix is applied repeatedly to the larger matrix, in the order that the larger matrix's
# inner arrays are defined. As such, this operation is akin to writing a loop to repeatedly apply the smaller
# matrix to different sections of the larger.
#   For column-based operations, one needs to construct the smaller matrix differently (here, it is spun using 
# the 'newaxis' command)
B = numpy.array([1, 2, 3])[:, numpy.newaxis]
print(A * B)
print(A + B)
print()
#   This method can also be used where the matrixes are the same size but different shapes
A = numpy.array([10, 20, 30])[:, numpy.newaxis]
B = numpy.array([1, 2, 3])
print(A * B)
print(A + B)
print()

# Cross Product / Vector Product
#   This is a binary operation on two vectors in three-dimensional space. The result is a vector which 
# is perpendicular to the vectors being multiplied and normal to the plane containing them. 
# This opperation can be performed with the command:
x = numpy.array( [0,0,1] )
y = numpy.matrix( [0,0,1] )
print( numpy.cross(x,y) )
print()








print("\n\n\n\n-- Editing An Array's Shape --")
# Flattening with ndarray's 'flatten' method
A = numpy.array(
    [
        [ 0,  1],
        [ 2,  3],
        [ 4,  5],
        [ 6,  7]
    ]
)
print( A )
print( A.flatten(order="C") ) # use C-style flattening (row-major) (default)
print( A.flatten(order="F") ) # use Fortran-style flattening (column-major)
print( A.flatten(order="A") ) # use Fortran-style if the array is Fortran contiguous in memory
print()

# Flattening with ndarray's 'ravel' method
print( A.ravel(order="C") ) # use C-style flattening (row-major) (default)
print( A.ravel(order="F") ) # use Fortran-style flattening (column-major)
print( A.ravel(order="A") ) # use Fortran-style if the array is Fortran contiguous in memory
print( A.ravel(order="K") ) # read the elements in whatever order that they occur in memory (except for reversing the data when strides are negative)
print()

# Reshaping with ndarray's 'reshape' method
print( A.reshape(2, 4, order="C") ) # use C-style flattening and construction (row-major) (default)
print( A.reshape(2, 4, order="F") ) # use Fortran-style flattening and construction (column-major)
print( A.reshape(2, 4, order="A") ) # use Fortran-style if the array is Fortran contiguous in memory
print()

# Concatenating
c = numpy.concatenate(
    (
        numpy.array([11,22]),
        numpy.array([18,7,6]),
        numpy.array([1,3,5])
    )
)
print(c) # all very simple
print()
# multidimensional concatenating must be done between matrixes of the same shape
#   the 'axis' attribute can be used to select which axis the concatenation occurs
#   with (default is 0)
print( 
    numpy.concatenate(
        (
            numpy.array(range(24)).reshape((3,4,2)),
            numpy.array(range(100,124)).reshape((3,4,2))
        )
    )
)
print( 
    numpy.concatenate(
        (
            numpy.array(range(24)).reshape((3,4,2)),
            numpy.array(range(100,124)).reshape((3,4,2))
        ),
        axis = 0
    )
)
print()

# Adding Dimensions
x = numpy.array([2,5,18,14,4])
print( x )
print( x[numpy.newaxis, :] ) # keeping the original array on the horizonal 
print( x[:, numpy.newaxis] ) # spinning the original array to vertical
print()

# Vector Stacking
vectorA = numpy.array([3, 4, 5])
vectorB = numpy.array([1, 9, 0])
print( numpy.row_stack(    (vectorA, vectorB) ) ) # stacking B upon A to create a matrix
print( numpy.column_stack( (vectorA, vectorB) ) ) # turning both array's 90deg and placing them side-by-side to create a matrix
print( numpy.column_stack( (vectorA, vectorA, vectorA) ) ) # multi stacking
print( numpy.dstack( (vectorA, vectorA, vectorA) ) ) # seems to do the same as before, except it also wraps everything in a array
print()





    


print("\n\n\n\n-- Matrixes --")
# the matrix class is a subclass of ndarray, as such it inherits much of ndarray's functionality, 
# though comes with the limitation that the dimension is set to 2. The class also rewrites some of
# the basic opperations to their matrix equivalents. 
a = numpy.matrix( ((2,3), (3, 5)) )
print( a )
# casting from a ndarray is also possible
a = numpy.mat( numpy.array( ((2,3), (3, 5)) ) )
print(a)
print()


# Matrix Product
#   The matrix product of two matrices can be calculated if the number of columns in the first matrix
# is equal to the number of rows in the second matrix
#   To do this, one can either use the 'numpy.dot' command
x = numpy.array( ((2,3), (3, 5)) )
y = numpy.matrix( ((1,2), (5, -1)) )
print( numpy.dot(x,y) )
#   or if both elements are of the matrix subtype; the asterisk
x = numpy.matrix( ((2,3), (3, 5)) )
y = numpy.matrix( ((1,2), (5, -1)) )
print( x * y )
print()

#   In the following example; four people have bought three amounts of chocolate, each from a different
# producer. The amounts they bought in grams are in the matrix below: 
NumPersons = numpy.matrix(
    [
        [100, 175, 210],
        [ 90, 160, 150],
        [200,  50, 100],
        [120,   0, 310]
    ]
)
# The price for each type of chocolate is in the following matrix
Price_per_100_g = numpy.array([2.98,3.90,1.99])

# Our task is to determine how much each person has to pay. So we can simple get the dot-product of 
# both matrixes, This will produce a matrix of one row with four numbers, each representing the cost
# to each person in cents. Then; one simply has to divide those numbers by 100 to get the euro amounts
Price_in_Cent = numpy.dot( NumPersons, Price_per_100_g )
print( Price_in_Cent / 100 )
print()