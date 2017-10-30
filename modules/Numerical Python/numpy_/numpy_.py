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