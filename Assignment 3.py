# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <your name>
# Collaborators : <your collaborators>
# Time spent    : <total time>

import math
import random


VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    print("Loading word list from file...")
    # inFile: file
    infile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in infile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # frequencies: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
    return freq


# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

    The score for a word is the product of two components:

    The first component is the sum of the points for letters in the word.
    The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

    Letters are scored as in Scrabble; A is worth 1, B is
    worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    word_score = 0
    for letter in word:
        word_score += SCRABBLE_LETTER_VALUES.get(letter)
    sum1 = (len(word)*7) - (n-len(word))*3
    if sum1 > 1:
        score2 = sum1
    else:
        score2 = 1
    total_score = word_score + score2
    return total_score


#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys():
        for position in range(hand[letter]):
            print(letter, end=' ')
    print()


#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand = {}
    num_vowels = int(math.ceil(n / 3))

    for letter in range(num_vowels):
        choice_vowel = random.choice(VOWELS)
        hand[choice_vowel] = hand.get(choice_vowel, 0) + 1
    
    for letter in range(num_vowels, n):
        choice_consonant = random.choice(CONSONANTS)
        hand[choice_consonant] = hand.get(choice_consonant, 0) + 1
    
    return hand


#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    new_hand = {}
    for letter in word:
        letter_frequency = hand.get(letter)
        if letter_frequency > 0:
            letter_frequency -= 1
        new_hand.update({letter: letter_frequency})
    for letter in hand:
        if letter not in word:
            letter_frequency = hand.get(letter)
            new_hand.update({letter: letter_frequency})
    return new_hand


#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    if word in word_list:
        for letter in word:
            if hand.get(letter) > 0:
                return True
            else:
                return False
    else:
        return False


#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    hand_length = 0
    for letter in hand:
        letter_value = hand.get(letter)
        hand_length += letter_value
    return hand_length


def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputting two
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    total_score = 0
    # new_hand = hand
    while hand != "":
        display_hand(hand)
        user_input = input("Please enter a word:")
        if user_input == "!!":
            break
        else:
            if is_valid_word(user_input, hand, word_list):
                total_score += get_word_score(user_input, calculate_handlen(hand))
                print("The word score is:", get_word_score(user_input, calculate_handlen(hand)))
            else:
                print("The word is not valid.")
            hand = update_hand(hand, user_input)
            hand_length = calculate_handlen(hand)
            new_hand = (deal_hand(7-hand_length))
            hand.update(new_hand)

    return total_score


#
# Problem #6: Playing a game
# 

#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    if letter in hand:
        substituted_hand = hand.copy()
        letter = letter.lower()
        letter_value = substituted_hand[letter]
        least_integer = math.ceil(letter_value / 3)
        del substituted_hand[letter]
        while sum(substituted_hand.values()) < sum(hand.values()):
            for key_value in range(least_integer):
                substituted_letter_v = random.choice(VOWELS)
                if substituted_letter_v not in hand:
                    substituted_hand[substituted_letter_v] = substituted_hand.get(substituted_letter_v, 0) + 1
            if sum(substituted_hand.values()) >= sum(hand.values()):
                break
            for key_value in range(least_integer, letter_value):
                substituted_letter_c = random.choice(CONSONANTS)
                if substituted_letter_c not in hand:
                    substituted_hand[substituted_letter_c] = substituted_hand.get(substituted_letter_c, 0) + 1
        return substituted_hand
    else:
        return hand

       
def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitute option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """

    substitute = 1
    replay = 1
    total_hands = int(input("Enter total number of hands: "))
    total_score = 0
    while total_hands >= 1:
        new_score = 0
        hand = deal_hand(HAND_SIZE)
        while substitute >= 1:
            print("Current hand:", end="  "), display_hand(hand)
            substitute_option = input("Would you like to substitute a letter: ")
            if substitute_option.lower() == "yes":
                letter = input("Which letter would you like to replace: ")
                hand = substitute_hand(hand, letter)
                substitute = substitute - 1
                break
            elif substitute_option.lower() == "no":
                break
        score = play_hand(hand, word_list)
        while replay >= 1:
            replay_option = input("Would you like to replay the hand: ")
            if replay_option.lower() == "yes":
                while substitute >= 1:
                    substitute_option = input("Would you like to substitute a letter: ")
                    if substitute_option.lower() == "yes":
                        letter = input("Which letter would you like to replace: ")
                        hand = substitute_hand(hand, letter)
                        substitute = substitute - 1
                        break
                    elif substitute_option.lower() == "no":
                        break
                new_score = play_hand(hand, word_list)
                replay = replay - 1
            elif replay_option == "no":
                break

        total_score += max(score, new_score)
        total_hands = total_hands - 1
    return total_score


#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    print("The total score is:", play_game(word_list))
    # print("The total score is:", get_word_score("bad", 7))
    # print("The remaining letters are:", update_hand({'a': 1, 'x': 2, 'l': 3, 'e': 1}, "axle"))
    # print("Is the word valid?:", is_valid_word("axle", {'a': 1, 'x': 2, 'l': 3, 'e': 1}, word_list))
    # print("The length of the hand is:", calculate_handlen({'a': 1, 'x': 2, 'l': 3, 'e': 1}))
    # user_hand = deal_hand(7)
    # print(user_hand)
    # display_hand(user_hand)
    # print("The total score is:", play_hand(user_hand, word_list))
    # print("The substituted hand is:", substitute_hand({'a': 1, 'x': 2, 'l': 3, 'e': 1}, "l"))
