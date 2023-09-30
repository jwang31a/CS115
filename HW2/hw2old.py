'''
Created on 9/28/23
@author:   Jun Hong Wang
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.
CS115 - Hw 2
'''
import sys
import dict
import bigdict as big

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

# print(letterScore("a", scrabbleScores))
# print(letterScore("c", scrabbleScores))

# print(wordScore("spam", scrabbleScores))
# print(wordScore("wow", [ ["o", 10], ["w", 42] ]))


def scoreList(Rack):
    """
    Rack is list of lower-case letters
    (helper 1)
    maybe choose a letter and see what words have this letter
    check that first word, see if enough letters given
    then next, and so on
    (helper 2)
    in order to keep track of words possible after each letter, another function needed
    pretty much just scoreList but defined with inputs Rack and wordlist
    (helper 3)
    all words that can be formed are returned along with their point values?
    """

    if Rack == []:
        return [[]]
    else:
        possible = filterWords(Rack, Dictionary)
        possible = repeatFilter(Rack, possible)
        return possible

"""
takes in a word and a Rack (list of chars)
finds out what letters are not in Rack using filter
return false if there is a letter in the word not in rack
true if all letters in word are in rack
"""
def lettersInWord(Rack, word):
    if word == "":
        return True
    elif word[0] in Rack:
        return lettersInWord(Rack, word[1:])
    else:
        return False
    
"""
given a word with repeat letters, figure out if list of chars can form that word
"""
def repeatCharFilter(chars, word, usedChars):
    if chars == []:
        return True
    elif word == "":
        return True
    else:
        # print("==============" + str(chars) + " === " + word)
        if word[0] in chars:
            i = findIndex(word[0], chars)
            usedChars += chars[i]
            return repeatCharFilter(chars[:i] + chars[i + 1:], word[1:], usedChars)
        else:
            return False

def findIndex(char, list):
    if list == []:
        return float("inf")
    elif char == list[0]:
        return 0
    else:
        return 1 + findIndex(char, list[1:])
    
def repeatFilter(chars, wordlist):
    # print(wordlist)
    if wordlist == []:
        return []
    else:
        if repeatCharFilter(chars, wordlist[0][0], []):
            return [wordlist[0]] + repeatFilter(chars, wordlist[1:])
        else:
            return repeatFilter(chars, wordlist[1:])

# wordlist = [['a', 1], ['am', 4], ['at', 2], ['spam', 8]]
# chars = ["a", "m", "p", "t", "s"]
# print(repeatFilter(chars, wordlist))

# spam = ["s", "p", "a", "m"]
# print(lettersInWord(spam, "spamm"))
    
"""
takes in a rack (or part of rack), a word, and a list of used chars called usedRack
returns the word if word can be constructed using chars in Rack, strictly
doesn't if letters to construct word not present
"""
def repeatWords(Rack, word, usedRack):
    if Rack == []:
        return ""
    else:
        if Rack[0] in word:
            usedRack += [Rack[0]]
            return repeatWords(Rack[1:], word ,usedRack)
        return ""
    
# apple = ["a", "p", "p", "l", "e"]
# aple = ["a", "p", "l", "e"]
# print(repeatWords(apple, "apple", []))
# print(repeatWords(aple, "apple", []))
 
"""
this is the actual scoreList bruh
(now I need to consider the case of duplicate letters)
"""
def filterWords(Rack, wordlist):
    if wordlist == []:
        return []
    else:
        if lettersInWord(Rack, wordlist[0]):
            return [[wordlist[0], wordScore(wordlist[0], scrabbleScores)]] + filterWords(Rack, wordlist[1:])
        else:
            return filterWords(Rack, wordlist[1:])
    
def getScore(words):
    if words == []:
        return []
    else:
        return [words[0][1]] + getScore(words[1:])

def bestWord(Rack):
    words = scoreList(Rack)
    if words == []:
        return ["", 0]
    else:
        indexBest = findIndex(max(getScore(words)), getScore(words))
        # print(indexBest)
        bestScore = words[indexBest]
        return bestScore

# print(bestWord(["a", "s", "m", "t", "p"]))
    
# w = [['a', 1], ['am', 4], ['at', 2], ['spam', 8]]
# print(getScore(w))

def scoreListDict(Rack, wordlist):
    wordlist = filterWords(Rack, wordlist)
    # print(wordlist)
    # print("===========" + str(wordlist) + " " + str(Rack))
    if Rack == []:
        return wordlist
    elif wordlist == []:
        return [[]]
    else:
        words = possibleWords(Rack[0], wordlist)
        if words == []:
            return scoreListDict(Rack[1:], wordlist)
        possible = possibleWords(Rack[0], wordlist)
        # possible = filterWords(Rack, possible)
        return scoreListDict(Rack[1:], possible)

def inWordlist(word, wordlist):
    if word in wordlist:
        return True
    else: 
        return False
    

# print(lettersInWord(["a", "b", "c", "e", "p"], "ape"))
# print(lettersInWord(["a", "b", "c", "e", "p"], "apple"))

# print(filterWords(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "r", "s"], ["sad", "age", "half"]))

    
def possibleWords(char, wordlist):
    if wordlist == []:
        return []
    elif char not in wordlist[0]:
        return possibleWords(char, wordlist[1:])
    else:
        return [wordlist[0]] + possibleWords(char, wordlist[1:])

# print(inWordlist("appple", Dictionary))

# r1 = ["a", "s", "m", "t", "p"]
# r2 = ["a", "s", "m", "o", "f", "o"]
# print(scoreList(r1))
# print(scoreList(r2))

# r3 = ["g", "y", "e"]
# print(bestWord(r3))

r4 = ['b', 'b', 'b', 'l', 'r', 'a', 'e']
print(bestWord(r4))
# print(Dictionary)

# print(filterWords(r1, Dictionary))
# print(filterWords(r2, Dictionary))

# print(possibleWords("a", Dictionary))
# print(possibleWords("g", Dictionary))
