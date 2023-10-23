#more tuples and dictionaries
#memoization next

import time, sys

sys.setrecursionlimit(2000)

"""
tuples kind of like equivalent of final keyword in java
"""

t = 123, 456, 789
print(len(t))

u = (12,)
print(type(u))

#fstrings, easier way of adding variable data into string
#syntactic sugar?
#assignment using a tuple
x, y, z = t
print(f"x = {x}, y = {y}, z = {z}")

#dictionaries, key value pairs
tel = {"jack": 4567, "jane" : 6789}
#to get keys as a list, use list()
print(tel)
# print(list(tel))
# print(list(tel.values()))
#dict.keys() and dict.values() to get keys and values (although not in list yet)
#if the key doesn't exist, new key created and value assigned
#if key exists, value is updated
tel["liz"] = 5678
print(tel)

#to delete a key value pair, use keyword del
del tel["jack"]
print(tel)

print("jack" in tel)
#function for empty dictionary if no arguments provided
empty = dict()
print(empty)

#when to use dict() vs {}? doesn't matter really (but it looks like {} is easier)
#to use dict() provide a list of tuples
votes = dict([ ("yes", 41), ("no", 37), ("absent", 67) ])
print(votes)

#memoization or optimizing recursion
#classic fib function, but inefficient
def fib(n):
    # print(n)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

print(time.time())

memo = {}
def fastFib(n):
    if n in memo:
        return memo[n]
    if n < 0:
        return "Incorrect"
    elif n == 0:
        memo[n] = 0
        return 0
    elif n == 1 or n == 2:
        memo[n] = 1
        return 1
    else:
        first_term = fastFib(n - 1)
        memo[n - 1] = first_term
        second_term = fastFib(n - 2)
        memo[n - 2] = second_term
        return first_term + second_term
    
"""
#memoization applied recursion is a lot faster
ta1 = time.time()
na1 = fib(20)
ta2 = time.time()

tb1 = time.time()
nb2 = fastFib(600)
tb2 = time.time()

print(ta2 - ta1, tb2 - tb1)
"""

memoLCS = {}
def fastLCS(s1, s2):
    if (s1, s2) in memoLCS:
        return memoLCS[(s1, s2)]
    if s1 == "" or s2 == "":
        memoLCS[(s1, s2)] = 0
        return 0
    elif s1[0] == s2[0]:
        common = 1 + fastLCS(s1[1:], s2[1:])
        memoLCS[(s1, s2)] = common
        return common
    else:
        use1 = fastLCS(s1, s2[1:])
        use2 = fastLCS(s1[1:], s2)
        answer = max(use1, use2)
        memoLCS[(s1, s2)] = answer
        return answer

print(fastLCS("spam", "sam"))
print(memoLCS)