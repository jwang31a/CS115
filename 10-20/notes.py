#shifting
"""
42 in base 10 left shifted is 420
42 right shifted is 4
"""

print("============")
print(42 << 1)
print(42 >> 1)

"""
binary addition testing
15 = 1111
10 = 1010

this one is for digits that stay
15 ^ 10
0101

carry
15 & 10
1010
then shift left

0111+0110 = 1101
"""

#doesn't actually return the binary representation of the number, but does it bitwise i guess
def binaryAddition(a, b):
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
        print(a, b)
    return a

print("============")
print(binaryAddition(15, 10))

"""
  binary multiplication
   111
  x101
  ----
   111
  000
 111
100011

5 x 6 = 30 = 16 + 8 + 4 + 2 = 11110
101 x 110 = 000 + 1010 + 10100 = 110
  000
 1010
10100
11110
"""

"""
Russian Peasant Multiplication
21 * 6 = 126
10 * 12
5 * 24
2 * 48
1 * 96
find the odd divided numbers, add the corresponding multiplied numbers
21, 5, 1 odd
6 + 24 + 96 = 126

in binary:
10101 * 110
1010 * 1100
101 * 11000
10 * 110000
1 * 1100000
10101, 101, 1 odd
110 + 11000 + 1100000
1111110 = 0 + 2 + 4 + 8 + 16 + 32 + 64 = 126

33 * 7 = 210 + 21 = 231
16 * 14
8 * 28
4 * 56
2 * 112
1 * 224
224 + 7
231
"""
"""
verify that 10101 * 110 is actually 126 in binary
why does russian peasant multiplication work?
"""
"""
the way that russian peasant multiplication works is that it treats base 10 numbers as base 2
the division by 2 is really a right shift, and the multiplication by 2 is really a left shift
my guess for why sum of odds:
when you right shift an odd number, you lose some value, so to get that value back, you take odd values
if value is even, you won't lose anything
"""