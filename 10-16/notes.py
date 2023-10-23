#no more recursion yay
#now move on to computer engineering
#using digital circuits to build computer?
#how computers do arithmetic
#assembly aaaaaaaaaaaaaaaaaaaaaaaaa

#number systems, like binary or base 10
"""
base b digits are 0 to b - 1
5 in base 2
101
in base 3
12
base 4
11
base 5
10
base 6
05
base 42
0(5)
number - integer multiple of biggest power of b, where integer is less than b that results in a positive int is 1, if doesn't subtract
if biggest integer multiple is 0, then that digit is 0
move on to the next digit
"""

#base 1 is unary

#to find the length of a number in a certain base, use logarithms with a specific base
#length = ceil(log10(100+1)), rounds to 3 even though the log is about 2
#discrete structures and discrete math?

#computers use base 2 (or hexadecimal but computers don't really use this)

#quiz
test = "hello", "how are you"
print(type(test))

memo = { "Istanbul" : 34, "Rome" : 45, "London" : 56 }
del memo["Rome"]
print(memo)

def multi(L, t = 1):
    if L == []:
        return t
    else:
        return multi(L[1:], t * L[0])
    
li = [1, 2, 3, 4, 5, 6]
print(multi(li))