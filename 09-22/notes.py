#lab 2 exercises from yesterday

def mySum(L):
    if L == []:
        return 0
    return L[0] + mySum(L[1:])

print(mySum([1, 2, 3, 4]))

"""
tracing the print statement
is [1, 2, 3, 4] empty? no
return 1 + mySum([1, 2, 3])
is [2, 3, 4] empty? no
1 + 2 + mySum([3, 4])
is [3, 4] empty? no
1 + 2 + 3 + mySum([4])
is [4] empty? no
1 + 2 + 3 + 4 + mySum([]) remember the last call!
= 10
"""

def reverseString(string):
    if string == "":
        return ""
    return reverseString(string[1:]) + string[0]

print(reverseString("friends"))
print(reverseString("tacocat"))
print(reverseString("racecar"))

def tribonacci(n):
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)

print(tribonacci(0))
print(tribonacci(1))
print(tribonacci(2))
print(tribonacci(3))
print(tribonacci(4))
print(tribonacci(5))
print(tribonacci(6))
print(tribonacci(7))
print(tribonacci(8))
print(tribonacci(9))
print(tribonacci(10))
