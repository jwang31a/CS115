#Jun Hong Wang
#HW1
# 9/14/23
# I pledge my honor that I have abided by the Stevens Honor System.
# CS115 HW-1

from functools import reduce


def factorial(n):
    l = createList(n)
    return reduce(mult, l)

#creates a list from 1 to n, inclusive
def createList(n):
    return list(range(1, n + 1))

def mult(x, y):
    return x * y

# print(factorial(4))
# print(factorial(5))
# print(factorial(6))

def mean(L):
    sum = reduce(add, L)/len(L)
    return sum

def add(x, y):
    return x + y

# thing1 = [1, 5, 6, 7]
# thing2 = [3, 3, 3, 3]
# thing3 = [2, 4, 6, 8, 10]

# print(mean(thing1))
# print(mean(thing2))
# print(mean(thing3))