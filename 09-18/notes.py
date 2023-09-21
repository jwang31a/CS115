#more lambda stuff

#works in interactive shell
"""
lambda x : x + 1
_(2) -> 3
only works for last previously defined lambda function
"""

#for this to work in IDE
increment = lambda x : x + 1
print(increment(2))

#other way is
print((lambda x, y, z: x * y ** z)(2, 3, 2))

higher_order_function = lambda x, f : x + f(x)

print(higher_order_function(3, lambda x : x ** 2))

try:
    higher_order_function(4, lambda x, y : x + y)
except:
    print("you get a typeerror since lambda only expects one argument")

print(higher_order_function(5, lambda scoobydoo : scoobydoo * 4))

def divides(n):
    def div(k):
        return n % k == 0
    return div

#f stores div, not the function
f = divides(10)
print(f(2))

listOfFunctions = [divides(10), divides(20)]
print(listOfFunctions[0](2))

#we sort based on index 1 of each tuple
#string sorting is just alphabetically ordering
pairs = [(1, "one"), (2, "two"), (3, "three"), (4, "four")]
pairs.sort(key = lambda pair : pair[1])
print(pairs)

#=======this isn't part of class notes, just me messing around
def myMap(func, l):
    for i in range(len(l)):
        l[i] = func(l[i])
    return l

print(myMap(lambda x : x ** 2, list(range(4))))

def myFilter(func, l):
    rlist = []
    for i in range(len(l)):
        if func(l[i]):
            rlist.append(l[i])
    return rlist

print(myFilter(lambda x : x % 2 == 0, [1,2,3,4,5,6,7,8,9]))

def myReduce(func, l):
    r = 0
    for i in range(len(l) - 1):
        if i == 0:
            r = func(l[i], l[i + 1])
        else:
            r = func(r, l[i + 1])
    return r

print(myReduce(lambda x, y : x * y, [1, 2, 3, 4, 5]))
#=======end goofy============================================