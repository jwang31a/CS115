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
    recursive function that alternates the values that are being compressed
    keeps recursively calling until input string S is empty
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

def binToNum(s):
    """
    converts binary to decimal
    """
    if s == "":
        return 0
    else:
        return int(s[-1]) + 2 * binToNum(s[:-1])

def uncompress(C):
    """
    takes compressed string and uncompresses it
    first uncompress to 0s, then 1s
    uses helper function alternator that has the bulk of this function's code
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

"""
question 1:
the maximum length of a string returned by compress would be 5 * 65 (325) if the input string alternates between 1 and 0, like 101010...
since the algorithm starts with compressing 0 first, there will be an extra 5 bits compared to if the string was 010101...

question 2:
the smallest length returned by the compression algorithm is 25, so the smallest ratio is about 0.39
the largest length is 325, so the largest ratio is about 5.08
using the example images, the ratio was low, below 1.5
it looks like the more 0s or 1s there are in a row, the lower the ratio (which makes sense)

question 3:
I've heard of "lossy" compression algorithms where information is lost after every compression run. 
I think this is why when images or videos get reposted, the quality gradually gets worse and worse and there's no way to recover the original from the lower quality one.
Professor Lai says that there's an algorithm that can always output a shorter string that represents an image, but using the example of reposting a compressed image or video, something is always lost.
Eventually, so much information is lost that it's unclear that the original file can't be recovered at all.
If you keep applying his algorithm to compress what's already been compressed, then you lose more and more information.
"""

seq1 = "01" * 32
print(compression(seq1))
seq2 = "10" * 32
print(compression(seq2))
seq3 = "0" * 64
print(compression(seq3))
seq4 = "00011000"+"00111100"*3 + "01111110"+"11111111"+"00111100"+"00100100"
print(compression(seq4))
seq5 = "0"*8 + "01100110"*2 + "0"*8 + "00001000" + "01000010" + "01111110" + "0"*8
print(compression(seq5))
seq6 = "1"*9 + "0"*7 + "10000000"*2 + "1"*7 + "0" + "00000001"*2 + "1"*7 + "0"
print(compression(seq6))
seq7 = "00000001" * 8
print(compression(seq7))
