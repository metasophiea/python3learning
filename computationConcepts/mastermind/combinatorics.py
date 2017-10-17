import random

def fac(n):
    """ factorial function: n! """
    if n == 0: return 1
    else:      return (fac(n-1) * n)

def k_permutations(items, n):
    """ yields every possible permutation of a list of length 'n', which only contains elements from the array 'items' """
    if n==0: yield []
    else:
        for i in range(len(items)):
            for ss in k_permutations(items, n-1):
                if (not items[i] in ss):
                    yield [items[i]]+ss

def permutations(items):
    """ yields every possible permutation of the array 'items' """
    return k_permutations(items,len(items))

def random_permutation(list):
    """ returns a random permutation  of the array 'items' """
    length = len(list);
    max = fac(length);
    index = random.randrange(0, max)
    i = 0
    for p in permutations(list):
        if i == index:
            return p
        i += 1

def all_colours(colours, positions):
    """ yields every possible permutation of a list of length 'n', which only contains elements from the array 'colours' which is in a randomized order """
    colours = random_permutation(colours)
    for s in k_permutations(colours, positions):
        yield(s)