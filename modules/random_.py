import random
# a module used to create random numbers







# Random
print( random.random() ) # generate a float between 0 and 1
print( random.randint(1,6) ) # generate an int between 1 and 6 (inclusive)
print()








# Seed
#   this command can be used to set the seed of the random number generator. Calling
# this command without arguments, sets the seed to the current time or from an operating
# system specific randomness source (if one is available)
# seed(a=None, version=2)
#   a           the seed
#   version     1 : the hash() of *a* is used
#               2 : (default) all of the bits are used if *a* is a str, bytes, or bytearray
#               if 'a' is an int; all bits are used
random.seed(0)
print( [ random.randint(1, 10) for x in range(10)] ) # print an array of 10 random numbers
random.seed(0)
print( [ random.randint(1, 10) for x in range(10)] ) # print an array of 10 random number
print()








# Choice
# this function selects a random element from a provided list, set, array, etc.
possibleLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
possibleThings  = ["sheep", "doughnut", 4, "paris", "an impending sense of dread"]
print( random.choice(possibleLetters) )
print( random.choice(possibleThings))
print()








# Sample
# this function produces an array/matrix of the specified size out of the provided elements
print( random.sample(range(1, 50), 6) )
print( random.sample(possibleThings, 5) ) # note: the specified size must be smaller that the number of provided elements
print()








# SystemRandom - Is used for cryptographically useful random number generation (using the machine's
# random number generator) (it also happens to be faster)
print( random.SystemRandom().random() )
print()

# here is an example of a random password generator that uses the SystemRandom submodule
def generate_password(length, valid_chars=None):
    """ generate_password(length, valid_chars) -> password
        length: the length of the created password
        valid_chars: a potential collection of allowed characters
    """

    if valid_chars==None:
        valid_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        valid_chars += valid_chars.lower() + "0123456789"
    
    password, sr = "", random.SystemRandom()
    while length > 0:
        char = chr(sr.randint(0, 128))
        if char in valid_chars:
            password += char
            length -= 1
            
    return password

print("Automatically generated password by Python: " + generate_password(16))