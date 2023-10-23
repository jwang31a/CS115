'''
Created on 10/18/23
@author:   Jun Hong Wang
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Lab 6
'''

def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    """
    42 in base 2 is 101010
    """
    return n % 2 != 0


def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    
    """
    base case n is 0, return ""
    otherwise, recursively call on n floor divided by 2, concatenate "1" if odd, concatenate "0" if even
    """
    if n == 0:
        return ""
    elif isOdd(n):
        return numToBinary(n // 2)  + "1"
    else:
        return numToBinary(n // 2) + "0"

# print(numToBinary(42))
# print(numToBinary(9))

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    """
    take the last character of string and add it to 2 * binaryToNum(rest of string)
    this way, each recursive call will multiply the value by 2, so the s[-1] would be multiplied by 1, s[-2] by 2, s[-3] by 4, and so on
    once the string becomes "", return 0
    """
    
    if s == "":
        return 0
    else:
        return int(s[-1]) + 2 * binaryToNum(s[:-1])
    
# print(binaryToNum("101010"))

def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    """
    input binary is converted into decimal, then incremented
    that result is then converted back into binary, but the number of digits might be off
    if there are missing digits, leads will be positive, and that amount of 0s will precede binary
    if the new binary is longer than the initial one, then cut off the first digits
    (since in this case, leads is negative, cut off the first -1 * leads bits)
    """
    
    n = binaryToNum(s) + 1
    b = numToBinary(n)
    leads = len(s) - len(b)
    if leads < 0:
        return b[-1 * leads:]
    return "0" * leads + b

# print(increment("00000000"))
# print(increment("00000001"))
# print(increment("00000111"))
# print(increment("11111111"))

def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    """
    first iteration prints n, so base case can't be n == 0 we want the last print statement
    call increment and input that into the recursive call
    """
    if n == -1:
        return
    inc = increment(s)
    print(s)
    return count(inc, n - 1)

# print("===========count prints==========")
# count("00000000", 4)

def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    """
    like binary, but with 3 modulo cases
    """
    if n == 0:
        return ""
    elif n % 3 == 0:
        return numToTernary(n // 3) + "0"
    elif n % 3 == 1:
        return numToTernary(n // 3) + "1"
    else:
        return numToTernary(n // 3) + "2"

# print(numToTernary(4242))

def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    """
    same as binaryToNum, except multiplies recursive call by 3
    """
    
    if s == "":
        return 0
    else:
        return int(s[-1]) + 3 * ternaryToNum(s[:-1])

# print(ternaryToNum("1120"))
# print(ternaryToNum("12211010"))

"""
answers to questions:
if a base-10 number is odd, the rightmost digit in its binary representation will be 1
if it's even, then the least significant bit will be 0

by eliminating the rightmost bit, it's equivalent to floor dividing by 2
if the rightmost bit is 0 (even), then floor division is division by 2
1010 -> 101, 10 -> 5
1011 -> 101, 11 -> 5

since y = n//2 (floor division), n either equals 2y or 2y + 1, depending on whether n is even or odd
so, shift y to the left by 1 bit and add a 0 at the end if n is even, add a 1 if n is odd
ex: 
y = 101, n = 1010 if n is even, n = 1011 if n is odd 

59 in ternary is 2012 because 2 * 3^0 + 1 * 3^1 + 0 * 3^2 + 2 * 3^3 = 2 + 3 + 0 + 54 = 59
each digit, represents a power of 3, starting from the right which is 3^0, then going to the left where the power increases by 1
"""