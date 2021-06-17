'''
    File: hangman.py
    Author: Drew Scott
    Description: A hangman game for 2 people.

    Important concepts to know before: if statements, loops, input, functions
    What's learned: lists
'''

def convert_to_blanks(s):
    '''
        Returns a string where are alpha chars in s are replaced with '_'
    '''

    blank_str = ''
    for c in s:
        if c.isalpha():
            blank_str += "_"
        else:
            blank_str += c

    return blank_str

def update_user_str(target, user_str, guess):
    '''
        Returns: inTarget -- True if guess in target, False otherwise
                 new_user_str -- updated user_str with '_' replaced with guess, corresponding to target

        Argument Requirements: target and user_str same length, and guess is one char and lower case
    '''

    new_user_str = ''
    inTarget = False
    for i in range(len(target)):
        if target[i].lower() == guess:
            new_user_str += target[i]
            inTarget = True
        else:
            new_user_str += user_str[i]
        
    return inTarget, new_user_str

def main():
    # get target string from player 1
    target = input("Player 1, input the target phrase:\n")
    print("Click enter until you can't see your input!")

    # set up player 2's info
    user_str = convert_to_blanks(target)
    user_guesses = []
    lives = 8
    user_lost = False

    # let player 2 guess
    while user_str != target:
        if lives <= 0:
            user_lost = True
            break

        # get their guess
        guess = input(f"You have {lives} lives, and have guessed {user_guesses}.\n{user_str}\nGuess a letter: ")
        guess_lower = guess.lower()

        # handle their guess
        if len(guess) != 1:
            print("You need to guess a single character")
            continue
        elif guess_lower in user_guesses:
            print(f"You already guessed {guess}. Try again.")
            continue
        else:
            inTarget, user_str = update_user_str(target, user_str, guess_lower)

            if not inTarget: 
                lives -= 1
            
            user_guesses.append(guess_lower)

    # game is over
    if user_lost == True:
        print(f"You lost! The correct phrase was:\n{target}")
    else:
        print(f"You guessed it!\n{target}")

if __name__ == '__main__':
    main()