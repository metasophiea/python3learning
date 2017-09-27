# Memoization is the process of wrapping a function in code which can remember past executions and pervious values when the input data matches input data of the past
# In Python; this can be accomplished manually or with the use of a decorator

# Below is an example of a simple memoization function

def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:            
            memo[x] = f(x)
        return memo[x]
    return helper

# This next function is a function used to generate values from the Fibonacci sequence - based on a position - in a recursive mannor.
# It's important to note here, that recursive calls are made to the memoized version of the function, thus benefiting from the efficiency improvement 

@memoize
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


print(fib(40))