"""
longest common subsequence
given two strings, return length of longest common subsequence
no common subsequence return 0

subsequence is a new string generated from original string (with some or 0 characters deleted) without changing relative order of characters

"ace" is subsequence is "abcde"
common subsequence of 2 strings is subsequence common to both strings

common known usage is comparing DNA
"""

def LCS(s1, s2):
    if s1 == "" or s2 == "":
        return 0
    elif s1[0] == s2[0]:
        return 1 + LCS(s1[1:], s2[1:])
    else:
        #if the chars are not the same
        use1 = LCS(s1, s2[1:])
        use2 = LCS(s1[1:], s2)
        #don't even need this lose case since use1 and use2 will default to lose if there is no equivalent
        # lose = LCS(s1[1:], s2[1:])
        return max(use1, use2)
    
print(LCS("AGGACAT", "ATTACGAT"))
print(LCS("spam", "sam!"))
print(LCS("spam", "xsam"))

"""
trace of LCS("spam", "sam")
1 + LCS("pam", "am")
    LCS("pam", "m")
        LCS("pam", "")
            return 0
        LCS("am", "am)
            return 1 + LCS("m", "m")
                return 1 + LCS("", "")
                    return 0
    2
3
    LCS("am", "am")
        return 1 + LCS("m", "m")
            return 1 + LCS("", "")
                return 0
    2

return 3
 
LCS("spam", "sam")
1 + LCS("pam", "am")
    max(LCS("pam", "m"), LCS("am", "am))
        max(LCS("pam", ""), LCS("am", "m"))
            return 0
        max(LCS("am", ""), LCS("m", "m))
            return 0
        1 + LCS("", "")
            return 0

etc, it's probably easier to do with hand than typing everything out     
there is also a trace function somewhere
"""

"""
tail recursion
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
#optimized for compiler since no more calculations in traceback, less memory used because stack doesn't have to remember traceback
#also easier compiler since after base case is reached, there is no more calculation to do, so directly returns final value
def factorialTail(n, a = 1):
    if n == 0:
        return a
    else:
        return factorialTail(n - 1, n * a)
    
print(factorial(5))
print(factorialTail(5))

def reverseString(word, newWord = ""):
    if word == "":
        return newWord
    return reverseString(word[0:-1], newWord + word[-1])

print(reverseString("racecar"))
print(reverseString("taco cat"))