#map, reduce, filter higher order functions

#to use reduce, we must import from functools
from functools import reduce

#we discussed map last time
#map(function(x), iterable sequence)
def add1(x):
    return x + 1

#map returns an object, not a list
print(list(map(add1, [0, 1, 2, 3])))

#reduce(function(x, y), iterable sequence)

def add(x, y):
    return x + y

#the result of reduce is one thing, not a list
print(reduce(add, [1, 2, 3, 4]))

#range function creates a list
thing1 = list(range(4)) #generates [0, 1, 2, 3], since the end is exclusive
thing2 = list(range(1, 5)) #generates [1, 2, 3, 4]

#note: range doesn't create a list, so we have to typecast it

print(thing1)
print(thing2)

#let's make a factorial function using reduce

def mult(x, y):
    return x * y

def factorial(n):
    return reduce(mult, range(1, n + 1))

print(factorial(4))
print(factorial(5))
print(factorial(6))

#filter(function(x), sequence)
#difference between filter and map is that function(x) returns a boolean, True or False

def isEven(x):
    return x % 2 == 0

print(list(filter(isEven, [1, 5, 7, 8, 10, 13])))
#if the function returns True, it will be included in the return, otherwise, it's filtered out