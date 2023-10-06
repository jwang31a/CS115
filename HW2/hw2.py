'''
Created on 9/28/23
@author:   Jun Hong Wang
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.
CS115 - Hw 2
'''

import sys

# Be sure to submit hw2.py.  Remove the '_template' from the file name.

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)

# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

# Implement your functions here.

def letterScore(letter, scorelist):
    """
    takes a letter and list of lists with letter and value as input
    empty list returns -1 (because score shouldn't be negative)
    if first list in scorelist has the letter, return the score
    otherwise recursively call letterScore with the same letter and the rest of the list
    """
    if scorelist == []:
        return 0
    elif scorelist[0][0] == letter:
        return scorelist[0][1]
    return letterScore(letter, scorelist[1:])

def wordScore(S, scorelist):
    """
    takes a string, checks if it's empty, if so, return 0
    otherwise, return the letterscore of the first letter and call wordscore on the rest of the list
    """
    if S == "":
        return 0
    return letterScore(S[0], scorelist) + wordScore(S[1:], scorelist)

def scoreList(Rack):
    """
    takes in Rack, list of chars
    returns a list of possible words and associated scores in 2D array
    uses a lot of helper functions to split up the code
    """
    if Rack == []:
        return [[]]
    else:
        possible = filterWords(Rack, Dictionary)
        possible = repeatFilter(Rack, possible)
        return possible

def filterWords(Rack, wordlist):
    """
    takes in a Rack, wordlist
    returns all words possible from wordlist using only characters in Rack
    (does not account for repeat characters)
    """
    if wordlist == []:
        return []
    else:
        if lettersInWord(Rack, wordlist[0]):
            return [[wordlist[0], wordScore(wordlist[0], scrabbleScores)]] + filterWords(Rack, wordlist[1:])
        else:
            return filterWords(Rack, wordlist[1:])

def repeatFilter(chars, wordlist):
    """
    takes in chars, wordlist, returns the words with strictly those chars
    (no repeats)
    """
    if wordlist == []:
        return []
    else:
        if repeatCharFilter(chars, wordlist[0][0], []):
            return [wordlist[0]] + repeatFilter(chars, wordlist[1:])
        else:
            return repeatFilter(chars, wordlist[1:])

def repeatCharFilter(chars, word, usedChars):
    """
    given a word with repeat letters, figure out if list of chars can form that word
    keeps track of used characters in another list
    returns True if all letters in word exist in chars, False if repeat letters
    """
    if chars == []:
        return True
    elif word == "":
        return True
    else:
        if word[0] in chars:
            i = findIndex(word[0], chars)
            usedChars += chars[i]
            return repeatCharFilter(chars[:i] + chars[i + 1:], word[1:], usedChars)
        else:
            return False

def lettersInWord(Rack, word):
    """
    takes in a word and a Rack (list of chars)
    finds out what letters are not in Rack using filter
    return false if there is a letter in the word not in rack
    true if all letters in word are in rack
    """
    if word == "":
        return True
    elif word[0] in Rack:
        return lettersInWord(Rack, word[1:])
    else:
        return False

def findIndex(char, list):
    """
    takes in a char and a list of chars, returns the first index in the list equal to char
    """
    if list == []:
        return float("inf")
    elif char == list[0]:
        return 0
    else:
        return 1 + findIndex(char, list[1:])
    
def getScore(words):
    """
    takes a list of words (2D array), returns the scores
    """
    if words == []:
        return []
    else:
        return [words[0][1]] + getScore(words[1:])

def bestWord(Rack):
    """
    runs scorelist to get the list of words possible with Rack
    returns ["", 0] if there are no words possible
    if there are words, gets the score of all the words, finds the index of the highest score
    then return the word with that index
    """
    words = scoreList(Rack)
    if words == []:
        return ["", 0]
    else:
        indexBest = findIndex(max(getScore(words)), getScore(words))
        bestScore = words[indexBest]
        return bestScore

def possibleWords(char, wordlist):
    """
    takes in a character and a wordlist (or dictionary)
    checks all words in wordlist with char and returns a list only with words with char
    """
    if wordlist == []:
        return []
    elif char not in wordlist[0]:
        return possibleWords(char, wordlist[1:])
    else:
        return [wordlist[0]] + possibleWords(char, wordlist[1:])

#=================test cases===================
print(filterWords(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "r", "s"], ["sad", "age", "half"]))