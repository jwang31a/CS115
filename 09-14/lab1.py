############################################################
# Name: Jun Hong Wang  
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
# CS115 Lab 1
#  
############################################################

from math import factorial
from functools import reduce

#helper to get taylor series through map
def inverse(x):
    return 1/x

# print(inverse(4))
# print(inverse(5))

"""
create a list with integers 0 through n
map the factorial (since 0! = 1)
then add up that taylor series and return result from reduce function
"""
def e(n):
    l = list(range(0, n + 1))
    fact = map(factorial, l)
    approx = reduce(add, map(inverse, fact))
    return approx

def add(x, y):
    return x + y

# print(e(2))

# print(factorial(5))
# print(factorial(0))