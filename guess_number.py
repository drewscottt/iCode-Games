'''
    File: guess_number.py
    Author: Drew Scott
    Description: When run, it allows user to play a guess the number game.
        The user can input the lower and upper bounds to guess between, and then starts guessing.

    Important concepts to know before: if statements, loops, input, functions
    What's learned: Error checking, design, basic string functions
'''

import random

def is_int(s):
    '''
        Returns True if s is a string equivalent to a valid integer (positive or negative)
    '''
    if s[ :1 ] == "-":
        return s[ 1: ].isnumeric()

    return s.isnumeric()

def set_bounds():
    '''
        Asks the user for lower and upper bounds for the game.
        It only accepts valid integers as bounds, and the upper bound must be >= to the lower bound.
    '''
    
    # get the lower bound
    lower_valid = False
    while not lower_valid:
        lower_bound = input("Enter lower bound: ")
        
        if is_int(lower_bound):
            lower_bound = int(lower_bound)
            lower_valid = True
        else:
            print("Lower bound must be a number")

    # get the upper bound
    upper_valid = False
    while not upper_valid:    
        upper_bound = input("Enter upper bound: ")

        if is_int(upper_bound):
            upper_bound = int(upper_bound)
            if upper_bound >= lower_bound:
                upper_valid = True
            else: 
                print(f"Upper bound must be >= {lower_bound}")
        else:
            print("Upper bound must be a number")

    return lower_bound, upper_bound

def update_bounds(guess, target, lower_bound, upper_bound):
    '''
        Returns: isHigh -- True if guess > target, False otherwise
                 lower_bound -- updated lower_bound (if guess < target and guess > lower_bound)
                 upper_bound -- updated upper_bound
    '''

    isHigh = False
    if guess > target:
        isHigh = True
        if guess < upper_bound:
            upper_bound = guess - 1

    elif guess < target and guess > lower_bound:
        lower_bound = guess + 1
    
    return isHigh, lower_bound, upper_bound

def handle_input(user_input, lower_bound, upper_bound, guesses):
    '''
        Returns True if 'quit' was input, False otherwise

        Prints out the appropriate text based on the user input
    '''

    if user_input == 'help':
        help_str = '''You have the following options:
        help : see this help text
        bounds : see your current lower and upper bound (inclusive)
        guesses : see how many guesses you have made
        quit : quit the game and see the correct target
        <int> : guess a number'''

        print(help_str)
    elif user_input == "bounds":
        print(f'Your bounds are: ({lower_bound}, {upper_bound}), inclusive')
    elif user_input == 'guesses':
        print(f'Your guesses: {guesses}')
    elif user_input == 'quit':
        return True
    else:
        print("Invalid input. Type 'help' to see valid options")

    return False

def main():
    # get upper and lower bounds
    lower_bound, upper_bound = set_bounds()
    
    # set the target value
    target = random.randint(lower_bound, upper_bound)

    # let user guess
    guesses = 0
    guessCorrect = False
    while not guessCorrect:
        user_input = input("Input guess: ")
        
        if is_int(user_input):
            guesses += 1
            guess = int(user_input)
            
            if guess == target: 
                guessCorrect = True
                break

            isHigh, lower_bound, upper_bound = update_bounds(guess, target, lower_bound, upper_bound)
            if isHigh:
                print("Guess too high")
            else:
                print("Guess too low")
        else: 
            isQuit = handle_input(user_input, lower_bound, upper_bound, guesses)
            if isQuit:
                break

    # game is over
    if guessCorrect:
        print(f'You guessed it in {guesses} guesses!')
    else: 
        print(f'You gave up. The target was {target}')

if __name__ == "__main__":
    main()