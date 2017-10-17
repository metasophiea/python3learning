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

def show_current_guess(new_guess):
    """ The current guess is printed to stdout """
    print("New Guess: ",end=" ")

    for c in new_guess:
        print(c, end=" ")
    print()
def inconsistent(permutation, guesses):
    """ the function checks, if a permutation, i.e. a list of 
    colours like 'permutation' = ['pink', 'yellow', 'green', 'red'] is consistent
    with the previous colours. Each previous colour permutation guess[0]
    compared with 'permutation' (using the check function) has to return the same amount of blacks 
    (rightly positioned colours) and whites (right colour at wrong 
    position) as the corresponding evaluation (guess[1] in the 
    list guesses) """
    for guess in guesses:
        res = check(guess[0], permutation)
        (rightly_positioned, permutated) = guess[1]
        if res != [rightly_positioned, permutated]:
            return True # inconsistent
    return False # i.e. consistent

def get_evaluation():
    """ asks the human player for an evaluation """
    show_current_guess(new_guess[0])
    rightly_positioned = int(input("Blacks: "))
    permutated = int(input("Whites: "))
    return (rightly_positioned, permutated)
def answer_ok(a):
    """ checking of an evaluation given by the human player makes 
    sense. 3 blacks and 1 white make no sense for example. """
    (rightly_positioned, permutated) = a
    if (rightly_positioned + permutated > gameWidth) or (rightly_positioned + permutated < len(colours) - gameWidth):
        return False
    if rightly_positioned == 3 and permutated == 1:
        return False
    return True
def view_guesses():
    """ The list of all guesses with the corresponding evaluations 
    is printed """
    print("Previous Guesses:")
    for guess in guesses:
        guessed_colours = guess[0]
        for c in guessed_colours:
            print(c, end=" ")
        for i in guess[1]:
            print(" %i " % i, end=" ")
        print()
def create_new_guess():
    """ a new guess is created, which is consistent to the 
    previous guesses """
    next_choice = next(permutation_iterator) 
    while inconsistent(next_choice, guesses):
        try:
            next_choice = next(permutation_iterator)
        except StopIteration:
            print("Error: Your answers were inconsistent!")
            return ()
    return next_choice

def new_evaluation(current_colour_choices):
    """ This funtion gets an evaluation of the current guess, checks 
    the consistency of this evaluation, adds the guess together with
    the evaluation to the list of guesses, shows the previous guesses 
    and creates a new guess """

    rightly_positioned, permutated = get_evaluation()
    if rightly_positioned == gameWidth:
        return(current_colour_choices, (rightly_positioned, permutated))
	
    if not answer_ok((rightly_positioned, permutated)):
        print("Input Error: Sorry, the input makes no sense")
        return(current_colour_choices, (-1, permutated))
    guesses.append((current_colour_choices, (rightly_positioned, permutated)))
    view_guesses()
	
    current_colour_choices = create_new_guess() 
    if not current_colour_choices:
        return(current_colour_choices, (-1, permutated))
    return(current_colour_choices, (rightly_positioned, permutated))


if __name__ == "__main__":
    colours = ["red","blue","green","black","white","yellow"]
    gameWidth = 4
    gameHeight = 12
    guesses = []	

    permutation_iterator = combinatorics.all_colours(colours, gameWidth)
    current_colour_choices = next(permutation_iterator)

    new_guess = (current_colour_choices, (0,0) )
    while (new_guess[1][0] == -1) or (new_guess[1][0] != gameWidth):
        new_guess = new_evaluation(new_guess[0])
