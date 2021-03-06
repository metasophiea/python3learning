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








# cumsum(a, axis=None, dtype=None, out=None)
#   this function returns the cumulative sum of the elements along a given axis as an array
print( numpy.cumsum([0.2,0.3,0.5]) ) # -> [0.2, 0.5, 1.0]
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
#       num         - number of samples to generate (default 50)

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








# meshgrid
#   Make N-D coordinate arrays for vectorized evaluations of N-D scalar/vector fields over N-D grids,
#   given one-dimensional coordinate arrays x1, x2,..., xn.

# This function appears to make a number of matrices out of a number of arrays. 

# In this example, three arrays are applied resulting is three items returned.
# these three items seems to hold the data for 3, 3-dimensional matrices: each 4x3x5
# the three matrices are made from the data of their corresponding input arrays, but with
# the data arranged in different ways

xlist = [10, 20, 30]
ylist = [1, 2, 3, 4]
zlist = [0, -1, -2, -3, -4] 
print(xlist)
print(ylist)
print(zlist)

X, Y, Z = numpy.meshgrid(xlist, ylist, zlist)
print(Y)
print(X)
print(Z)
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
print()

# Choice - for selecting a item from a array at random
#   in this example, we select a profession from a list, while also providing
# the (optional) probabilities attribute to weight the professions
professions = ["scientist", "philosopher", "engineer", "priest", "programmer"]
probabilities = [0.2, 0.05, 0.3, 0.15, 0.3]

outcomeCounters, testCount = {}, 1000
for a in range(testCount):
    selection = numpy.random.choice(professions, p=probabilities)
    if selection not in outcomeCounters: outcomeCounters[selection] = 1
    else:                                outcomeCounters[selection] += 1

for item in outcomeCounters:
    print( item+":", outcomeCounters[item]/testCount, end="    " )
print()
print()








# Saving and Loading Data with a Text File
#   This is a command for saving numpy mathematical data into a text file 
# savetxt(fname, X, fmt='%.18e', delimiter=' ', newline='\n', header='', footer='', comments='# ')
#   fname       - output file name
#   X 	        - 'array_like' data to be saved to the text file
#   fmt         - format of the printed string (or sequence of strings)(optional)
#   delimiter   - A string used for separating the columns
#   newline     - A string which will end a line
#   header 	    - A String that will be written at the beginning of the file.
#   footer 	    - A String that will be written at the end of the file.
#   comments    - A String that will be prepended to the 'header' and 'footer' strings, to mark them 
#                   as comments. The hash tag '#' is used as the default.

x = numpy.array(
    [
        [1, 2, 3], 
        [4, 5, 6],
        [7, 8, 9]
    ]
)

numpy.savetxt(
    "test.txt", 
    x,
    fmt="%2.3f",
    delimiter="|"
)

y = numpy.loadtxt(
    "test.txt",
    delimiter="|"
)
print(y)
print()








# Saving Loading Data with a File
#   A simpler and perhaps frankly better approach to saving data to file
x = numpy.array(
    [
        [1, 2, 3], 
        [4, 5, 6],
        [7, 8, 9]
    ]
)
numpy.save("savedData", x)

y = numpy.load("savedData.npy")
print( y )
print()








# linalg
# this method is used for solving Linear Combinations
# A linear combination in mathematics is an expression constructed from a set of terms by
# multiplying each term by a constant and adding the results.

# (3.21, 1.77, 3.65) and the unit vectors (0,0,1), (0,1,0) and (1,0,0)
# (3.21, 1.77, 3.65) = 3.21 · (1,0,0) + 1.77 (0,1,0) + 3.65 · (0,0,1) 
x = numpy.array([[0,0,1],[0,1,0],[1,0,0]])
y = ([3.65,1.55,3.42])
print( numpy.linalg.solve(x,y) )
print()

# (3.21, 1.77, 3.65) and the unit vectors (0,1,1), (1,1,0) and (1,0,1)
x = numpy.array([[0,1,1],[1,1,0],[1,0,1]])
y = ([3.65,1.55,3.42])
print( numpy.linalg.solve(x,y) )
print()