import random, numpy

def find_interval(x, partition, endpoints=True):
    # this function finds the location of the value 'x' in the 
    # sorted array 'partition', if it were to be inserted
    # (if 'endpoints' is set to True, -1 will be returned if 'x'
    # is not within the bounds of the array 'partition', otherwise
    # the function will return 0 or the length of the array)
    """ find_interval -> i
        If endpoints is True, "i" will be the index for which applies
        partition[i] < x < partition[i+1], if such an index exists.
        -1 otherwise
        
        If endpoints is False, "i" will be the smallest index 
        for which applies x < partition[i]. If no such index exists 
        "i" will be set to len(partition)
    """
    for i in range(0, len(partition)):
        if x < partition[i]:
            return i-1 if endpoints else i
    return -1 if endpoints else len(partition)

def weighted_choice(sequence, weights, secure=True):
    # this function selects a random element of the sequence based 
    # on the provided array of weights
    """
        the function creates a cumulative list of values based on the
        provided weights; then creates a random number and finds which
        interval that number falls into. The selected interval is the
        selected element from the sequence
    """

    cum_weights = [0] + list(numpy.cumsum(weights))
    if secure:  x = random.SystemRandom().random()
    else:       x = numpy.random.random()
    index = find_interval(x, cum_weights)
    return sequence[index]




# testing a weighted dice
faces_of_die = [1, 2, 3, 4, 5, 6]
weights = [1/12, 1/6, 1/6, 1/6, 1/6, 3/12]
outcomeCounts = [0, 0, 0, 0, 0, 0]
testCount = 1000

for a in range(testCount):
    outcomeCounts[weighted_choice(faces_of_die, weights)-1] += 1

print("Testing a weighted dice:")
for item in outcomeCounts:
    print( item/testCount, end="\t" )
print("\n")
# notice how '1' appeared the least while '6' appeared the most








def weighted_sample(population, weights, k):
    # this function selects 'k' items from the array 'population' based
    # on their weights (which are stored in the array 'weights')
    #   In this particular version of the function; each time an element
    # is selected, it is removed from the arrays 'population' and 'weights'
    # with the 'weights' array values being recalculated to maintain the
    # "sum-to-one" aspect of the values
    """ 
    This function draws a random sample of length k 
    from the sequence 'population' according to the 
    list of weights
    """
    sample = set()
    population = list(population)
    weights = list(weights) 
    while len(sample) < k:
        choice = weighted_choice(population, weights)
        sample.add(choice)

        index = population.index(choice)
        weights.pop(index)
        population.pop(index)

        weights = [ x / sum(weights) for x in weights] # recalculate weights

    return list(sample)

def weighted_sample_alternative(population, weights, k):
    # this function selects 'k' items from the array 'population' based
    # on their weights (which are stored in the array 'weights')
    #   In this particular version of the function; the random weighted selection
    # occurs repeatedly until 'k'  unique selections are made
    """ 
    Alternative way to previous implementation.
        
    This function draws a random sample of length k 
    from the sequence 'population' according to the 
    list of weights
    """
    sample = set()
    population = list(population)
    weights = list(weights)
    while len(sample) < k:
        choice = weighted_choice(population, weights)
        if choice not in sample:
            sample.add(choice)
    return list(sample)



# out of a random sample of three elements from the 'balls' array; how often does
# orange come out?

balls = ["red", "green", "blue", "yellow", "black", "white", "pink", "orange"]
weights = [ 1/24, 1/6, 1/6, 1/12, 1/12, 1/24, 1/8, 7/24]

n = 100
orange_counter = 0
orange_counter_alternative = 0
for i in range(n):
    if "orange" in weighted_sample(balls, weights, 3):
        orange_counter += 1
    if "orange" in weighted_sample_alternative(balls, weights, 3):
        orange_counter_alternative += 1 
        
print("Taking a weighted sample:")
print(orange_counter / n)
print(orange_counter_alternative / n)
print()








def cartesian_choice(*iterables):
    """
    A list with random choices from each iterable of iterables 
    is being created in respective order.
    
    The result list can be seen as an element of the 
    Cartesian product of the iterables 
    """
    res = []
    for population in iterables:
        res.append(random.choice(population))
    return res

def weighted_cartesian_choice(*iterables):
    """
    A list with weighted random choices from each iterable of iterables 
    is being created in respective order
    """
    res = []
    for population, weight in iterables:
        lst = weighted_choice(population, weight)
        res.append(lst)
    return res

print("A Cartesian Choice:")
print( 
    cartesian_choice(
        ["The", "A"],
        ["red", "green", "blue", "yellow", "grey"], 
        ["car", "house", "fish", "light"],
        ["smells", "dreams", "blinks"]
    )
)
print()

print("A Weighted Cartesian Choice:")
determiners = (
    ["The", "A", "Each", "Every", "No"], 
    [0.3, 0.3, 0.1, 0.1, 0.2]
)
colours = (
    ["red", "green", "blue", "yellow", "grey"], 
    [0.1, 0.3, 0.3, 0.2, 0.2]
)
nouns = (
    ["water", "elephant", "fish", "light", "programming language"], 
    [0.3, 0.2, 0.1, 0.1, 0.3]
)
nouns2 = (
    ["of happiness", "of chocolate", "of wisdom", "of challenges", "of air"], 
    [0.5, 0.2, 0.1, 0.1, 0.1]
)
verb_phrases = (
    ["smells", "dreams", "thinks", "is made of"], 
    [0.4, 0.3, 0.2, 0.1]
)


print("It may or may not be true:")
for i in range(10):
    res = weighted_cartesian_choice(determiners,colours,nouns,verb_phrases,nouns2)
    print(" ".join(res) + ".")