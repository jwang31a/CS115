"""
1 question on list slicing/indexing
1 question on string slicing/indexing
2 on higher order functions
2 recursion tracing
1 recursive function writing
1 use it or lose it
8 questions total

strict on syntax
"""

from functools import reduce

#example problems
try:
    names = ["Liz", "Jack", "May", "John"]
    colors = ["blue", "red", "green"]
    C = names[-2: 0: -1] + colors[2:] + [names[1]]
    print(C)
except:
    print("TypeError: can only concatenate list (not 'str' to list)")
# can be solved if [] around names[1]

className = "Physics"
adjectives = "fun boring hard"
print(className + adjectives[10:] + ", man")
print(className + adjectives[-5:] + ", man")

#returns n^2
def mystery(n):
    if n == 0:
        return 0
    return mystery(n - 1) + 2 * n - 1

print(mystery(3))
# print(mystery(4))
# print(mystery(2))
# print(mystery(15))

"""
mystery(3)
    return mystery(2) + 2 * 3 - 1
        return mystery(1) + 2 * 2 - 1
            return mystery(0) + 2 * 1 - 1
                return 0
            0 + 1 = 1
        1 + 4 - 1 = 4
    4 + 6 - 1 = 9
return 9
"""

"""
write a recursive function "findLess" that takes a list of numbers and an integer n as an input and returns a list of numbers in the given list that are less than n
"""
def findLess(List, n):
    if List == []:
        return []
    elif List[0] < n:
        return [List[0]] + findLess(List[1:], n)
    else:
        return findLess(List[1:], n)
    
print(findLess([1, 6, 3, 5, 8], 6))
print(findLess([6, 6, 6, 6, 6], 6))

"""
write a function "factorial" that takes a two numbers indicating start and end of a range (but start will be 1?) and find factorial by using higher order lambda and range functions
"""
def factorial(start, end):
    return reduce(lambda x, y: x * y, range(start, end + 1))

print(factorial(1, 5))