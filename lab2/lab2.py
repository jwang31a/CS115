"""
#Name: Jun Hong Wang
#Pledge: I pledge my honor that I have abided by the Stevens Honor System.
#Date: 9/21/23
#Lab 2: Recursion
"""

"""
input: L and K, both lists
if not equal length, return 0
if they are, multiply L[0], K[0] then add the dot product of the rest
"""
def dot(L, K):
    if L == [] and K == []:
        return 0
    elif recursiveLength(L) != recursiveLength(K):
        #since the lists are not of equal length, to return 0, just return 0 at some point
        return 0
    return L[0] * K[0] + dot(L[1:], K[1:])

"""
a recursively defined length function for lists
slightly different from the one in class since I did it differently
"""
def recursiveLength(List):
    l = 0
    if List[0:1] == []:
        # print(List[0:1])
        return l
    l += 1 + recursiveLength(List[0 : -1])
    return l

#test cases for length and dot product
# print(recursiveLength([]))
# print(recursiveLength([1,2,3,4,5,6]))
# print(recursiveLength([1]))

# vec1 = [5,3]
# vec2 = [6,4]
# vec3 = [1,2,3]
# print(dot(vec1, vec2))
# print(dot(vec1, vec3))

"""
input: string
if empty string, return empty list
otherwise, return list with first character, then call function on rest of string
"""
def explode(S):
    if S == "":
        return []
    return [S[0]] + explode(S[1:])

# print(explode("spam"))
# print(explode(""))
# print(explode(" "))

"""
input: takes element e and sequence L, where e is element we want to find in L
if L is empty list or string, return 0
if e is at L[0], return 0
otherwise, return 1 + ind(e, rest of list)
output: integer as index
if the element isn't in L, index will be length of list
"""
def ind(e, L):
    if L == [] or L == "":
        return 0
    if e == L[0]:
        return 0
    return 1 + ind(e, L[1:])

#test cases copied from pdf
# print(ind(42, [55, 77, 42, 12, 42, 100]))
# print(ind(42, range(0, 100)))
# print(ind("hi", ["hello", 42, True]))
# print(ind('hi', [ 'well', 'hi', 'there' ]))
# print(ind('i', 'team'))
# print(ind(' ', 'outer exploration'))

"""
input: element e and list L, 
output: return the list with all instances of e gone
if e isn't in the list, return the list as is
otherwise, call remove all with the first instance of e removed

"""
def removeAll(e, L):
    index = ind(e, L)
    if index == recursiveLength(L):
        return L
    return removeAll(e, L[0:index] + L[index + 1:])
    
#copied test cases
# print(removeAll(42, [ 55, 77, 42, 11, 42, 88 ]))
# print(removeAll(42, [ 55, [77, 42], [11, 42], 88 ]))
# print(removeAll([77, 42], [ 55, [77, 42], [11, 42], 88 ]))

"""
inputs: a function that returns a boolean value and a list
output: that same list, but only with the values that returned true through the function
base case is empty list, then return an empty list
if the function returns True for a value, return that value in its own list + myfilter(rest of list)
if returns False, returns myfilter(rest of list)
"""
def myFilter(func, L):
    if L == []:
        return []
    if func(L[0]):
        #reason that L[0] is in list is so that a list is returned at the end
        return [L[0]] + myFilter(func, L[1:])
    return myFilter(func, L[1:])

#even function for myfilter
def isEven(x):
    return x % 2 == 0

#divisible by 5
def isDivBy5(x):
    return x % 5 == 0

#my own test cases
# print(myFilter(isEven, list(range(20))))
# print(myFilter(isDivBy5, list(range(100))))

"""
input: list where there may be nested lists
output: list with reversed order of elements, and reversed order of the elements in nested lists
if the list is empty, return empty list
if L[0] is a list, return a deepreverse of the rest of the list + a deepreverse of L[0]
if L[0] isn't a list, deepreverse the rest of the list then addf L[0] in its own list
"""
def deepReverse(L):
    # print(L)
    if L == []:
        return []
    elif isinstance(L[0], list):
        return deepReverse(L[1:]) + [deepReverse(L[0])]
    else:
        return deepReverse(L[1:]) + [L[0]]
    
# print(deepReverse([1, 2, 3]))
# print(deepReverse([1, [2, 3], 4]))
# print(deepReverse([1, [2, [3, 4], [5, [6, 7], 8]]]))