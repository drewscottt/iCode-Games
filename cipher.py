'''
    File: cipher.py
    Author: Drew Scott
    Description: Cipher guessing game for 2 people.

    Important concepts to know before: if statements, loops, input, functions
    What's learned: lists, dictionaries, strings, ASCII
'''

import random
from hangman import convert_to_blanks

def get_letters():
    '''
        Returns a list of all lower case letters
    '''

    letters = []
    for i in range(97, 123):
        letters.append(chr(i))

    return letters

def create_cipher(letters, shuffled):
    '''
        Returns a dictionary where each letter in letters is mapped to the corresponding letter in shuffled
    '''
    cipher = {}
    for i in range(len(letters)):
        letter = letters[i]
        shuffled_letter = shuffled[i]

        cipher.update({letter : shuffled_letter})

    return cipher

def encode(target, cipher):
    '''
        Returns a string where target is encoded by the cipher dictionary
    '''

    encoded_str = ''
    for c in target:
        if c in cipher.keys():
            encoded_str += cipher.get(c)
        else:
            encoded_str += c
    
    return encoded_str

def is_valid_mapping(mapping):
    '''
        Returns: True if mapping is of the form 'a b', where a and b must be alpha chars, False otherwise
    '''

    if len(mapping) != 3:
        return False
    
    if not mapping[0].isalpha():
        return False
    elif mapping[1] != ' ':
        return False
    elif not mapping[2].isalpha():
        return False
    
    return True

def update_user_guess(user_guess, encoded, map_from, map_to):
    '''
        Returns an updated user_guess string where map_from chars in encoded are changed to map_to
        chars in new_user_guess
    '''

    new_user_guess = ''
    for i in range(len(encoded)):
        if encoded[i].lower() == map_from:
            new_user_guess += map_to
        else:
            new_user_guess += user_guess[i]

    return new_user_guess

def get_counts_str(encoded):
    '''
        Returns a string of the frequency of each letter in encoded string
    '''

    # create counts dict
    counts = {}
    for c in encoded:
        if not c.isalpha():
            continue

        if c in counts.keys():
            counts.update({c : counts.get(c) + 1})
        else:
            counts.update({c : 1})

    # create counts string
    counts_str = 'Counts: '
    for c in counts.keys():
        counts_str += f"{c}: {counts.get(c)}, "

    counts_str = counts_str[:-2]

    return counts_str

def main():
    # set up cipher
    letters = get_letters()
    shuffled = letters.copy()
    random.shuffle(shuffled)
    cipher = create_cipher(letters, shuffled)

    # get target
    target = input("Player 1, input target phrase:\n")
    target_lower = target.lower()

    print("Click enter until you can't see your input!")

    # create encoded and user guess string
    user_guess_str = convert_to_blanks(target)
    encoded_str = encode(target_lower, cipher)

    while user_guess_str != target_lower:
        # get mapping
        mapping = input(f"{user_guess_str}\n{encoded_str}\nEnter a mapping: ")
        if mapping == "counts":
            print(get_counts_str(encoded_str))
        elif is_valid_mapping(mapping):
            user_guess_str = update_user_guess(user_guess_str, encoded_str, mapping[0], mapping[2])
        else:
            print("Invalid mapping. Correct format: 'a b'. Or 'counts'")

    print(f"You got it!\n{target}")


if __name__ == "__main__":
    main()