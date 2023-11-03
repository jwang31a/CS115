'''
Created on 10/31/2023
@author:   Jun Hong Wang
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 6
'''
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.

def findEndIndex(S):
    """
    S is rest of string from compress, since part of original string is cut off
    this only returns the end index, so add 1 to get length of substring
    base case 1 is no length string or string of length 1
    base case 2 is different chars, so return 0
    otherwise, recursively call function on rest of string and add 1
    """
    # print(S)
    if len(S) == 0 or len(S) == 1:
        return 0
    if S[0] != S[1]:
        return 0
    else:
        return 1 + findEndIndex(S[1:])
    
# testS = "0" * 63
# print(findEndIndex(testS))
# print(findEndIndex("0"))
#     
def decToBin(n):
    """
    decimal to binary function to make converting differences in index into binary for compress easier
    """
    if n == 0:
        return ""
    elif n % 2 != 0:
        return decToBin(n // 2)  + "1"
    else:
        return decToBin(n // 2) + "0"
    
def compress(S):
    """
    takes in a string, length 64
    returns binary string as output, representing run-length encoding of input
    size of compressed block determined by variable above
    max length of compressed block is max run length above
    always start with trying to compress 0?
    following uncompress using helper function with n alternating
    """
    return compressAlternator(S, "0")

def compressAlternator(S, n):
    """
    repeats is 1 + endIndex b/c we want to include the first index (0)
    """
    if S == "":
        return ""
    if S[0] != n and n == "0":
        return COMPRESSED_BLOCK_SIZE * "0" + compressAlternator(S, "1")
    elif S[0] != n and n == "1":
        return COMPRESSED_BLOCK_SIZE * "0" + compressAlternator(S, "0")
    else:
        repeats = findEndIndex(S) + 1
        b = decToBin(repeats)
        extra = (COMPRESSED_BLOCK_SIZE - len(b)) * "0"
        if repeats > MAX_RUN_LENGTH:
            b = decToBin(MAX_RUN_LENGTH)
            if n == "0":
                return b + compressAlternator(S[MAX_RUN_LENGTH:], "1")
            else:
                return b + compressAlternator(S[MAX_RUN_LENGTH:], "0")
        if n == "0":
            return extra + b + compressAlternator(S[repeats:], "1")
        else:
            return extra + b + compressAlternator(S[repeats:], "0")



    # if S == "":
    #     return ""
    # # print(S, S[0])
    # currEnd = findEndIndex(S) + 1
    # #there's a chance that currEnd is higher than max run length, so just let the first 31 and run again on the rest
    # if currEnd > MAX_RUN_LENGTH:
    #     b = decToBin(MAX_RUN_LENGTH)
    #     currEnd = 31
    #     return b + COMPRESSED_BLOCK_SIZE * "0" + compress(S[currEnd:])
    # else:
    #     b = decToBin(currEnd)
    #     extra = ""
    #     if len(b) <= 5:
    #         extra = (5 - len(b)) * "0"
    #     if S[0] == "1" and extra != "":
    #         return extra + b + compress(S[currEnd:])
    #     elif S[0] == "1" and extra == "":
    #         return "0" * COMPRESSED_BLOCK_SIZE + extra + b + compress(S[currEnd:])
    #     else:
    #         return extra + b + compress(S[currEnd:])


# print(compress("0" * 64))

def binToNum(s):
    if s == "":
        return 0
    else:
        return int(s[-1]) + 2 * binToNum(s[:-1])

def uncompress(C):
    """
    takes compressed string and uncompresses it
    first uncompress to 0s, then 1s
    could possibly do this with another variable default set to 0 in this function?
    """
    return uncompressAlternator(C, "0")
    
def uncompressAlternator(C, n):
    """
    n is what number function is uncompressing
    n should alternate after every function call
    """
    if C == "":
        return ""
    multiplier = binToNum(C[:5])
    if n == "0":
        return multiplier * n + uncompressAlternator(C[5:], "1")
    else:
        return multiplier * n + uncompressAlternator(C[5:], "0")

# comp = compress("0" * 64)
# print(uncompress(comp))

def compression(S):
    """
    takes the length of compressed string and divides by length of uncompressed string
    """
    L = len(compress(S))
    return L / len(S)

# seq = '0' * (MAX_RUN_LENGTH + 1) + '1' * (MAX_RUN_LENGTH + 1) + '0' * (64 - 2 * MAX_RUN_LENGTH - 2)
# ans = '111110000000001111110000000001'
# # print(seq + "\n")
# # print(uncompress(compress(seq)))
# print(compress(seq))
# # print(ans)