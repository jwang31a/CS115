"""
integers (int)
floating point (float)
string (str)
"""

#type() returns the type of the input
print(type(4))

#typecasting
print(int(3.14))
print(float(14))

#string concatenation
name = "joe"
greeting = "welcome "
print("welcome " + name)

#also f strings
name = "bobby"
print(f"welcome {name}")

#string multiplication exists
print("f to pay respects " * 3)

#string subtraction (or division) doesn't exist
try:
    print(name - 3)
except:
    print("you goofed up")

try:
    print(name / 3)
except:
    print("stop")

#lower() and upper() functions (this can also be done using ASCII)
print("a".upper())

#functions
def functionName(x):
    #r = 2 * x
    #return r
    return 2 * x

def main():
    print(functionName(5))

main()
