#to represent signed integers, leftmost bit is the sign bit
"""
0101 represents 5
1101 represents -5
problem is that after incrementing enough, you go from max value to min value
there is also a possibility of -0

5 + -5
 0101
 1101
10010, 2
6 + -2
 0110
 1010
10000, -0
addition is problematic

all of this is based on registers
4 bit operations will result in 4 bit results
overflow bits are possible

one's complement
the negative of a positive integer is not the number, so
0010 is 2
1101 is -2

1000 -7
1001 -6
1010 -5
...
1111 -0
0000 0

problem still arises with -0 and addition
(ignore overflow)
5 + -5
 0101
 1010
11111, -0 = 0
5 + -3
 0101
 1100
10001, 1
6 + -2
 0110
 1101
10011, 3

two's complement
one's complement + 1 to find negative equivalent
1000 -8
1001 -7
1010 -6
...
1111 -1
0000 0

this way, the negation of 0 is still 0

5 + -5
 0101
 1011
10000, -0

6 + -2
 0110
 1110
10100, (ignoring overflow, since that goes somewhere else, 4)
math finally works

this stuff is based in computer engineering

converting -4 to base 2:
0100 (unsigned binary)
one's complement:
1011
two's complement:
1100

double check: -8 + 4 = -4
-25 to base 2
25 in base 2:
00011001
one's complement:
11100110
two's complement:
11100111
to check:
-128 + 64 + 32 + 4 + 2 + 1
-128 + 103 = -25

in unsigned numbers, 5 bits would represent 25, but in signed world, -25 has to be represented by 6 bits
1 bit is for the sign, and the rest represent numbers
"""

"""
-30 in 6 bits
30 in 6 bits:
011110
one's complement:
100001
two's complement:
100010

check:
-32 + 2 = -30

-11 in 8 bits
11 in 8 bits:
00001011
one's complement
11110100
two's complement
11110101

check:
1 + 4 + 16 + 32 + 64 + -128
117 - 128 = -11

smallest possible 8 bit number, -256, -2^8
largest 8 bit number, 255, 2^8 - 1
"""