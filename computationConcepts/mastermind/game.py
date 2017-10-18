import combinatorics

def check(rootPermutation, newPermutation):
    """ this calculates the number of bulls (blacks) and cows (whites) of two permutations """
    blacks, whites = 0, 0
    for i in range(len(rootPermutation)):
        # check perfect placement
        if newPermutation[i] == rootPermutation[i]:
            blacks += 1
        else:
            # check if the value is present at all
            if newPermutation[i] in rootPermutation: 
                whites += 1
    return [blacks, whites] 

def showCurrentGuess(new_guess):
    """ The current guess is printed to stdout """
    print("New Guess: ",end=" ")
    for colour in new_guess:
        print(colour, end=" ")
    print()
def isInconsistent(permutation, guesses):
    """ this function goes through all the previous guesses, generating 
    black/white values against the provided permutation 'permutation'.
    These values are compared to the user provided black/white values
    which are attached to each guess. If at any point the generated and
    provided black/white values are different; there is an inconsistency.
    """

    for guess in guesses:
        res = check(guess[0], permutation)
        if res != [guess[1][0], guess[1][1]]: # [correctlyPositioned, correctlyPresent]
            return True # inconsistent
    return False # consistent

def getEvaluation():
    """ asks the human player for an evaluation on the current guess"""
    showCurrentGuess(newGuess[0])
    return (int(input("Blacks: ")), int(input("Whites: ")))
def answerOk(answerData):
    """ checking that the evaluation given by the human player makes sense """
    # answerData => [correctlyPositioned, correctlyPresent]
    if  (answerData[0]+answerData[1] > gameWidth) or \
        (answerData[0]+answerData[1] < len(colours)-gameWidth) or \
        (answerData[0] == 3 and answerData[1] == 1):
        # black + white is beyond game size (eg. "10 correct values in your guess of 4 values")
        # black + white is below logical possibility
        # 3 blacks and 1 white (that white has nowhere else to go)
        return False
    return True
def viewGuesses():
    """ prints out all previous guesses """
    print("Previous Guesses:")
    for guess in guesses:
        # some spacing
        print("   ", end=" ")

        # print permutation
        for colour in guess[0]: print(colour, end=" ")
        print("-", end=" ")

        # print black/white values
        for val in guess[1]: print(val, end=" ")
        print()
def createNewGuess():
    """ generate new permutations with the iterator, checking to see if they are 
    consistent/valid guesses. Once a consistent/valid one is found, return it. If
    the iterator runs out of permutations; return an inconsistency error"""

    while True:
        nextChoice = next(permutationIterator, None)
        if nextChoice == None:
            print("Error: Your answers were inconsistent!")
            return None
        elif not isInconsistent(nextChoice, guesses):
            return nextChoice

def newEvaluation(currentColourGuess):
    """ this function:
        - gets an evaluation from the human of the current guess
        - checks if evaluation is ok
        - checks if its a win situation
        - appends the latest guess to the list of incorrect guesses, then prints them all out
        - produce a new guess (end the game if we're out of permutations, otherwise; return the guess with the current evaluation)
    """

    # get an evaluation from the human of the current guess
    correctlyPositioned, correctlyPresent = getEvaluation()
	
    # check if evaluation is ok
    if not answerOk((correctlyPositioned, correctlyPresent)):
        print("Input Error: Sorry, the input makes no sense")
        return(currentColourGuess, (-1, correctlyPresent))

    # win situation
    if correctlyPositioned == gameWidth:
        return(currentColourGuess, (correctlyPositioned, correctlyPresent))

    # append this guess to the list of incorrect guesses, then print them out
    guesses.append((currentColourGuess, (correctlyPositioned, correctlyPresent)))
    viewGuesses()
	
    # produce a new guess (end the game if we're out of permutations, otherwise; return the guess with the current evaluation)
    currentColourGuess = createNewGuess() 
    if currentColourGuess == None:
        return None
    return(currentColourGuess, (correctlyPositioned, correctlyPresent))

if __name__ == "__main__":
    colours = ["red","blue","green","black","white","yellow"]
    gameWidth = 4
    gameHeight = 12
    guesses = []	

    permutationIterator = combinatorics.all_colours(colours, gameWidth)
    currentColourChoices = next(permutationIterator)

    newGuess = (currentColourChoices, (0,0) )
    while newGuess != None and ((newGuess[1][0] == -1) or (newGuess[1][0] != gameWidth)):
        newGuess = newEvaluation(newGuess[0])
