"""
Wordle Clone Project.

HOW TO PLAY

Guess the WORDLE in six tries.

Each guess must be a valid five-letter word. Hit the enter button to submit.

After each guess, the color of the tiles will change to show how close your guess was to the word.

Examples

ACTUAL WORD :: W E A R Y
GUESS WORD  :: W B C D F
The letter W is in the word and in the correct spot. Hence W will be colored GREEN.

ACTUAL WORD :: P I L L S
GUESS WORD  :: A E I O U
The letter I is in the word but in the wrong spot. Hence I will be colored YELLOW.

ACTUAL WORD :: V A G U E
GUESS WORD  :: B C D F G
The letter B is not in the word in any spot. Hence B will be colored GREY.

"""

# UNIVERSAL CONSTANTS
# URL list provided in the assignment
WORDS_DICTIONARY_URL = "https://raw.githubusercontent.com/charlesreid1/five-letter-words/master/sgb-words.txt"
# NUMBER OF LETTERS IN THE WORDS TO GUESS
LENGTH_OF_WORD = 5
# NUMBER OF EACH TRY USER GETS TO GUESS WORD
NUMBER_OF_TRIES = 6

import requests

# Colorama Library is used to print colored text in terminal.
# We can avoid using this library by using ANSI escape sequences in the string for example,
# 
# HEADER = '\033[95m'
# OKBLUE = '\033[94m'
# OKCYAN = '\033[96m'
# OKGREEN = '\033[92m'
# WARNING = '\033[93m'
# FAIL = '\033[91m'
# ENDC = '\033[0m'
# BOLD = '\033[1m'
# UNDERLINE = '\033[4m' etc etc...
# 
# I used this library because it was better for code readibility.
from colorama import Fore

# This needs an active internet connection to work, 
# in case there is no internet, this code will default to
# hardcoded words
try:
    res = requests.get(WORDS_DICTIONARY_URL)
    words = [ x for x in res.text.splitlines() ]
except requests.exceptions.RequestException:
    words = ["WEARY", "PILLS", "VAGUE"]

# Randomize word from the list to avoid predictability
# If you want to pick any particular word from the list then, replace
# 
# word = words[random.randint(0, len(words))].upper()
# 
# with line
# 
# word = words[0].upper() 
# 
# Where 0 means the first word from the list
from random import randint
word = words[randint(0, len(words))].upper()

counter = 0

# ask user to guess the word within the specified amount of tries
while counter < NUMBER_OF_TRIES:
    print("Please Enter {0} Letter Word".format(LENGTH_OF_WORD))
    guess_word = input().upper() # using upper() on whole string to match is better than to use upper() on each character in loop to match.

    # If the length of word is not same then I am not counting it as a try.
    # If this needs to be counted as a try, then we can add
    # 
    # counter = counter + 1
    # 
    # before continue
    if len(guess_word) != LENGTH_OF_WORD:
        print("Number Of Letters Are Not Same") 
        continue

    # Here each letter is matched, color coded as per Wordle rules and printed on terminal for user to guess.
    output = ""
    for i in range(0, LENGTH_OF_WORD):
        if guess_word[i] == word[i]: # check for letter in exact location
            output = output + Fore.GREEN + guess_word[i] + " "
        elif guess_word[i] in word: # if above condition fails that means character at this location (i) is not same, hence checking it for any other location
            output = output + Fore.YELLOW + guess_word[i] + " "
        else: # letter is nowhere to be found in the word
            output = output + Fore.LIGHTBLACK_EX + guess_word[i] + " "
    print(output+Fore.RESET)
    
    # If user guess the word in any of the mentioned number of tries. he wins and the loop is exited
    if guess_word == word:
        print("You Guessed The Correct Word")
        break

    # else if the user exhaust all number of tries then this program shows user the correct word and the loop exits.
    elif counter == NUMBER_OF_TRIES - 1:
        print("Wrong Guess The Correct Word Was "+ Fore.RED + "{0}".format(word) + Fore.RESET)

    counter = counter + 1

