"""
Notes: 
arithmetic operations of python
normal mathematics operators: +, -, *, / (remember that / is normal division)
as well as % (modulus), // (floor division), ** (exponentiation)

"""

# expression that finds average of 32, 12, 46: (keep in mind order of operations)
# also keep in mind values returned/printed (we want an integer, not a float)
print((32 + 12 + 46) // 3)
# alternatively, typecast it
print(int((32 + 12 + 46) / 3))

# another expression
print((4 * (8 - 5)) // ((2 ** 3) - 7))
# always a good idea to put parentheses

#variables!
x = 5 # = is assignment operator, this line just means x has been assigned the value 5
#equality operator is ==
print(x == 5)
#remember that boolean values are capitalized

"""
variable naming conventions:
no numbers in first character
be careful of punctuation, especially if it has other uses
don't use keywords
multi assignment
"""

x, y, z = 1, 2, 3
print(x, y, z)

#increment/decrement operators (works with other operations too)
x += 2
print(x)
x = x + 2
print(x)

#strings
user = "Stevens"
print(user[0])
print(len(user))
#remember -1 and minus indexing