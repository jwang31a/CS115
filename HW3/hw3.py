'''
Created on 10/20/23
@author:   Jun Hong Wang
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 3
'''

import sys

sys.setrecursionlimit(1500)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 0
' Implement the function giveChange() here:
' See the PDF in Canvas for more details.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# your code goes here
    
def giveChange(amount, coins):
    """
    input of integer amount, list of coins
    similar design to previous lab, where a list is generated through a helper function
    number of coins is length of list generated
    returns list, index 0 is int with number of coins, index 1 is list of all coins used
    """
    coinList = giveChangeHelper(amount, coins)
    return [len(coinList), coinList]
    
def giveChangeHelper(amount, coins):
    """
    helper function for giveChange that takes in int amount and list of coins
    if amount is 0, return empty list
    if coins is empty, return inf
    if first coin > amount, call giveChangeHelper(amount, rest of list)
    else, use it or lose it to figure out which list uses fewer coins, return that one
        also figure out if any of the lists sums to infinity, if so, don't use that list
    """
    if amount == 0:
        return []
    elif coins == []:
        return [float("inf")]
    elif coins[0] > amount:
        return giveChangeHelper(amount, coins[1:])
    else:
        """
        if the sum of values is infinity, return the other one
        if both are not infinity, figure out which list is shorter
        """
        use = [coins[0]] + giveChangeHelper(amount - coins[0], coins)
        lose = giveChangeHelper(amount, coins[1:])
        # print(use, lose)
        change_use = sum(use)
        change_lose = sum(lose)
        if change_use == float("inf"):
            return lose
        elif change_lose == float("inf"):
            return use
        else:
            if min(len(use), len(lose)) == len(use):
                return use
            else:
                return lose

# def sum(coinList):
#     return reduce(lambda x, y : x + y, coinList)
# print(giveChange(48, [1, 5, 10, 25]))

# print(giveChange(48, [50, 25, 10, 5, 1]))

# Here's the list of letter values and a small dictionary to use.
# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 1
' Implement wordsWithScore() which is specified below.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def wordsWithScore(dct, scores):
    '''List of words in dct, with their Scrabble score.

    Assume dct is a list of words and scores is a list of [letter,number]
    pairs. Return the dictionary annotated so each word is paired with its
    value. For example, wordsWithScore(Dictionary, scrabbleScores) should
    return [['a', 1], ['am', 4], ['at', 2] ...etc... ]
    '''
    if dct == []:
        return []
    else:
        return [[dct[0], wordScore(dct[0], scores)]] + wordsWithScore(dct[1:], scores)

#letterscore and wordscore taken from my work in previous homework
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

# print(wordScore("am", scrabbleScores))
# print(wordsWithScore(Dictionary, scrabbleScores))

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 2
' For the sake of an exercise, we will implement a function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
' (Notice that you cannot assume anything about the length of the list.)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def take(n, L):
    '''Returns the list L[0:n], assuming L is a list and n is at least 0.'''
    print(n, L)
    if n == 0 or L == []:
        return []
    else:
        return [L[0]] + take(n - 1, L[1:])

print(take(10, ["hello"]))

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 3
' Similar to problem 2, will implement another function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def drop(n, L):
    '''Returns the list L[n:], assuming L is a list and n is at least 0.'''
    if n == 0:
        return L
    else:
        return drop(n - 1, L[1:])

