# map(func, seq)
# func - some input function
# seq - a sequence of objects (eg. list) upon which the func will be applied one by one
# this function returns an iterator or the results

# using a regular function
def usualFunction(input):
    return input*2

print(list( map(usualFunction,[1,2,3,4]) ))

# using a lambda function
print(list( map( (lambda input : input*2) ,[1,2,3,4]) ))


# the map function also allows multi-input functions using multiple sequence inputs (where all the sequences are the same length)
seq_1 = [1,2,3,4]
seq_2 = [1,2,3,4]
seq_3 = [1,2,3,4]
lambdaFunc = lambda x,y,z : x+y+z

print(list(    map(lambdaFunc,seq_1,seq_2,seq_3)     ))