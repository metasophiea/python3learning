import numpy
#   This module provides fast precompiled functions for mathematical and numerical routines as well as
# adding powerful data structures for efficient computation of multi-dimensional arrays and matrices with 
# a large library of high-level mathematical functions to operate on these matrices and arrays.



# mat(data, dtype=None)
#    This function converts the 'data' (usually a two-dimensional vector) to a matrix
#       data  - input data
#       dtype - Data-type of the output matrix
x = numpy.array(
    [
        [1, 2], 
        [3, 4]
    ]
)
m = numpy.mat(x)
print( type(x) )
print( x )
print( type(m) )
print( m )
# operations between matrixes comply with regular matrix operations
a = numpy.mat( [[1,2],[3,4]] )
b = numpy.mat( [[5,6],[7,8]] )
print( a*b ) # matrix multiplication
print()




# arange([start,] stop[, step,], dtype=None)
#   This function returns evenly spaced values within a given interval (alot like 'range')
print( numpy.arange(1, 10) )
print( numpy.arange(10.4) )
print( numpy.arange(0.5, 10.4, step=0.8) )
print( numpy.arange(0.5, 10.4, step=0.8, dtype=int) )
print()

# linspace(start, stop, num=50, endpoint=True, retstep=False)
#   linspace returns an ndarray, consisting of 'num' equally spaced samples in the interval
#       start       - defines the start value of the sequence
#       stop        - defines the end value of the sequence (unless 'endpoint' is set to False, in which 
#                     case the resulting sequence will consist of all but the last of 'num + 1' evenly 
#                     spaced samples, excluding stop)
#       endpoint    - determines whether a closed or half-open interval will be returned
#       retstep     - if set, the function will also return the value of the spacing between adjacent 
#                     values (returning a tuple)

# 50 values between 1 and 10:
print( numpy.linspace(1, 10) )
# 7 values between 1 and 10:
print( numpy.linspace(1, 10, num=7) )
# excluding the endpoint:
print( numpy.linspace(1, 10, num=7, endpoint=False) )
print()

print( numpy.linspace(1, 10, retstep=True)[1] )
print( numpy.linspace(1, 10, 20, endpoint=True, retstep=True)[1] )
print( numpy.linspace(1, 10, 20, endpoint=False, retstep=True)[1] )
print()








# tile(inputMatrix, tilingMultiplier)
#   This command is used to produce a matrix out of repeatidly tiling a provided matrix
print( numpy.tile(numpy.array([0, 1, 2]), (3,1)) ) # take this row, and return three of them stacked
print( numpy.tile(numpy.array([1]),(3,3)) ) # take this one value, and produce a 3x3 matrix of it
print()








# random - the numpy's submodule for generating random numbers
print( numpy.random.random() ) # generates a random float between 0 and 1
print( numpy.random.random(2) ) # returns a list of the requested number of random float numbers
print( numpy.random.random((3,3)) ) # returns a matrix of the requested number of random float numbers
print( numpy.random.random_sample((3,3)) ) # returns a matrix of the requested number of random float numbers
print( numpy.random.randint(1, 7) ) # generate an int between 1 and 7
print( numpy.random.randint(1, 7, size=10) ) # returns a list of the requested number of ints between 0 and 7
print( numpy.random.randint(1, 7, size=(3,3)) ) # returns a matrix of the requested number of ints between 0 and 7
# note: the generation method is not suitable for cryptographic use
print()

# Random Numbers Satisfying sum-to-one Condition
#   in this case, one wants a list of random floats that sum to 1
randomFloatList = numpy.random.random(3)
normalizedRandomFloatList = randomFloatList/randomFloatList.sum()
print( normalizedRandomFloatList, "sum to:", normalizedRandomFloatList.sum() )



