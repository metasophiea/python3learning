import numpy
#   This module provides fast precompiled functions for mathematical and numerical routines as well as
# adding powerful data structures for efficient computation of multi-dimensional arrays and matrices with 
# a large library of high-level mathematical functions to operate on these matrices and arrays.



# The ndarray Object
#   Used within the numpy module as the main data type for storing items. 

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
print(B)
print("The dimension of array:", numpy.ndim(B)) 
print()


# array shape
#   this function returns a tuple of numbers representing the dimensions of the array
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
print(numpy.shape(x))
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