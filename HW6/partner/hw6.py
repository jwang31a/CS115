'''
Created on 11/2/2023
@author:   RJ Toothill & Jun Hong Wang
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

def toBinary(n,pos=2**(COMPRESSED_BLOCK_SIZE-1),res=''):
    '''
    Takes a base-10 number (n), converts it to binary and pads it to
    COMPRESSED_BLOCK_SIZE using tail recusrion
    '''
    if(pos==0):
        return res
    elif(n-pos<0):
        return toBinary(n,pos//2,res+'0')
    else:
        return toBinary(n-pos,pos//2,res+'1')

def fromBinary(n,pos=2**(COMPRESSED_BLOCK_SIZE-1),res=0):
    '''
    Takes a binary string (n), converts it to base-10 using tail recusion
    '''
    if(pos==0):
        return res
    else:
        x = int(n[0])*pos
        return fromBinary(n[1:],pos//2,res+x)
    
def seqlen(S,bit,res=0):
    '''
    Takes a string of binary digits and the bit that is being analyzed (bit),
    returns a tuple containing the length of the sequence of bit, that length
    in binary, and the remianing string not including those bits
    '''
    if(S == '' or S[0] != bit or res >= MAX_RUN_LENGTH):
        return (res,toBinary(res),S)
    else:
        return seqlen(S[1:],bit,res+1)

def compress(S):
    '''
    Takes a string of binary (S), returns the compressed string using
    run-length-encoding
    '''
    if(S==''):
        return ''
    else:       
        r0 = seqlen(S,'0')
        if(r0[2] == ''):
            return r0[1]
        r1 = seqlen(r0[2],'1')
        return r0[1]+r1[1]+compress(r1[2])

    '''
    QUESTION 1:

    The largest number of bits that the "compress" algorithm will use to encode
    a 64-bit string is 325. This would happen if there is 1 back square followed
    by a while square. This is because each sequence of white or black is
    5 bits, and 5 * 64 is 320, plus 5 more bits for the 00000 at the begininng,
    representing it starting with no 0s.
    '''

def uncompress(S):
    '''
    Takes a string of run-length-encoded binary (S), returns the uncompressed
    binary
    '''
    if(S==''):
        return ''
    else:
        r0 = fromBinary(S[:COMPRESSED_BLOCK_SIZE]) * '0'
        c1 = S[COMPRESSED_BLOCK_SIZE:2*COMPRESSED_BLOCK_SIZE]
        if(c1 == ''):
            return r0
        r1 = fromBinary(c1) * '1'
        return r0+r1+uncompress(S[COMPRESSED_BLOCK_SIZE*2:])

def compression(S):
    '''
    Takes a string of binary (S), returns the ratio of the length of the
    compressed string compared to uncompressed
    '''
    return len(compress(S))/len(S)

    '''
    QUESTION 2

    I tested 5 different cases with the compression ratios. I tested the 3
    images in "hw6.pdf," as well as the longest possible compressed string
    and shortest possible compressed string. I found that the max ratio is
    about 5.07 while the minimum is 0.39. The average is about 1.8 based off
    the 5 data points.

    The more places where the bits change, the bigger the file will be.
    '''

    '''
    Question 3
    Laicompress cannot exist because run-length-encoding needs to be standard
    across the entire string. If your compressed string is a mixed of
    uncompressed bits plus compressed blocks, the uncompress fuction wont be
    able to destinguish the two and would either reproduce a completely
    different image or cause an error.

    Additionally, in the real world, there's "lossy" compression algorithms 
    where information is lost every time in exchange for smaller file sizes.
    The problem with lossy compression algorithms is that the original data
    is unrecoverable. Whenever a video or image is reposted enough, the 
    quality will visibly get worse to a point that the original file is 
    completely unobtainable.
    In general, if this algorithm can always return a shorter string, then 
    if we compress the ccompressed string, then we get an even smaller string.
    If we repeatedly apply his compression algorithm, then we'll lose so much 
    information that the original is completely unobtainable.
    '''

