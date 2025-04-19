"""
Author: Sanju Jacob
UID:292593
Location : Trivandrum UST main campus
"""


# importing required liberaries

import string
from itertools import permutations
# function1

# Creating functions
def getspan(s, r):

    # intializing counters

    count = 0

    spans = []

    start = 0

    while True:

        start = s.find(r, start)

        if start == -1:
            # breaking the loop
            break
            # getting index of end
        end = start + len(r)

        spans.append((start, end))

        count += 1

        start += 1  # Move to the next character to find subsequent occurrences

    return count, spans
 # function2
# reversing a string
def reverse_string(a):

    if not isinstance(a, str):
        a = str(a)  # Convert non-string inputs to string
    return ''.join(reversed(a))



# function3 :Remove punctuation from a string
def remove_punctuation(word: str) -> str:
    return word.translate(str.maketrans('', '', string.punctuation))

# functions 4 : Counts the number of words in s

def count_words(s):
    return len(s.split())

# function 5 :
# Returns a dicƟonary with characters of s as keys and their frequencies as values.

def characterMap(s):
    char_map = {}
    for char in s:
        char_map[char] = char_map.get(char, 0) + 1
    return char_map 

# function 6:

def makeTitle(s):
    return s.title()

# function 7:
#normalizeSpaces(s) – Removes extra spaces, leaving only single spaces between words

def normalizeSpaces(s):
    return ' '.join(s.split())


# function 8
#transform(s) – Reverses the string and swaps case (e.g., "Hello" → "OLLEh"
def transform(s):
    return s[::-1].swapcase()

# function 9
# Returns all permutaƟons of the string s. 

def getPermutations(s):
    return [''.join(p) for p in permutations(s)]



if __name__ == "__main__":
    pass
