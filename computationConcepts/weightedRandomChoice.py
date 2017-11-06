import random, numpy

def find_interval(x, partition):
    # this function finds the location of the value 'x' in the 
    # sorted array 'partition', if it were to be inserted
    """ find_interval -> i
        partition is a sequence of numerical values
        x is a numerical value
        The return value "i" will be the index for which applies
        partition[i] < x < partition[i+1], if such an index exists.
        -1 otherwise
    """

    for i in range(0, len(partition)):
        if x < partition[i]:
            return i-1
    return -1

def weighted_choice(sequence, weights, secure=True):
    # this function  selects a random element of the sequence based 
    # on the provided array of weights

    if secure:  x = random.SystemRandom().random()
    else:       x = numpy.random.random()
    cum_weights = [0] + list(numpy.cumsum(weights))
    index = find_interval(x, cum_weights)
    return sequence[index]





# testing a weighted dice
faces_of_die = [1, 2, 3, 4, 5, 6]
weights = [1/12, 1/6, 1/6, 1/6, 1/6, 3/12]
outcomeCounts = [0, 0, 0, 0, 0, 0]
testCount = 1000

for a in range(testCount):
    outcomeCounts[weighted_choice(faces_of_die, weights)-1] += 1

for item in outcomeCounts:
    print( item/testCount, end="\t" )
print()
# notice how '1' appeared the least while '6' appeared the most