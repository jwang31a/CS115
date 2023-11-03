# mandelbrot.py
# Lab 9
# 11/2/2023
# Name: Jun Hong Wang
# I pledge my honor that I have abided by the Stevens Honor System.

# keep this import line...
from cs5png import PNGImage

# start your Lab 9 functions here:

def mult(c, n):
    """
    multiplication without multiplication operator (using addition and loop)
    n is guaranteed to be an integer so that's why range(n) is valid
    """
    result = 0
    for i in range(n):
        result += c
    return result

print("mult test cases")
print(mult(5, 6))
print(mult(6, 7))
print(mult(1.5, 28))

def update(c, n):
    """
    takes in c and n, keeps doing z^2 + c, n times, then returns final z value
    """
    z = 0
    for i in range(n):
        z = z**2 + c
    return z

print("update test cases")
print(update(1, 3))
print(update(-1, 3))
print(update(1, 10))
print(update(-1, 3))

def inMSet(c, n):
    """ inMSet takes in
    c for the update step of z = z**2+c
    n, the maximum number of times to run that step
    Then, it should return
    False as soon as abs(z) gets larger than 2
    True if abs(z) never gets larger than 2 (for n iterations)
    """
    z = 0 + 0j
    for i in range(n):
        z = z**2 + c
        if abs(z) > 2:
            return False
    return True

c1 = 0 + 0j
c2 = 3 + 4j
c3 = 0.3 + -0.5j
c4 = -0.7 + 0.3j
c5 = 0.42 + 0.2j
print("inmset test cases")
print(inMSet(c1, 25))
print(inMSet(c2, 25))
print(inMSet(c3, 25))
print(inMSet(c4, 25))
print(inMSet(c5, 25))
print(inMSet(c5, 50))

def weWantThisPixel( col, row ):
    """ a function that returns True if we want
    the pixel at col, row and False otherwise
    """
    if col%10 == 0 or row%10 == 0:
        return True
    else:
        return False
    
def test():
    """ a function to demonstrate how
    to create and save a png image
    """
    width = 300
    height = 200
    image = PNGImage(width, height)
    # create a loop in order to draw some pixels
    for col in range(width):
        for row in range(height):
            if weWantThisPixel( col, row ) == True:
                image.plotPoint(col, row)
    # we looped through every image pixel; we now write the file
    image.saveFile()
    """
    if col % 10 == 0 and row % 10 == 0 was changed to
    if col % 10 == 0 or row % 10 == 0, then there would be a grid
    """

# test()

def scale(pix, pixMax, floatMin, floatMax):
    """ scale takes in
    pix, the CURRENT pixel column (or row)
    pixMax, the total # of pixel columns
    floatMin, the min floating-point value
    floatMax, the max floating-point value
    scale returns the floating-point value that
    corresponds to pix
    """
    f = floatMax - floatMin
    p = 1.0*pix / pixMax
    return f * p + floatMin

print(scale(100, 200, -2.0, 1.0))
print(scale(100, 200, -1.5, 1.5))
print(scale(100, 300, -2.0, 1.0))
print(scale(25, 300, -2.0, 1.0))
print(scale(299, 300, -2.0, 1.0))

def mset():
    """ 
    creates a 300x200 image of the Mandelbrot set
    uses scale function to map value to coordinate
    """
    width = 300#3840
    height = 200#2160
    image = PNGImage(width, height)
    # create a loop in order to draw some pixels
    for col in range(width):
        for row in range(height):
            # here is where you will need
            x = scale(col, width, -2.0, 1.0)
            y = scale(row, height, -1.0, 1.0)
            c = x + y*1j
            n = 25
            # to create the complex number, c!
            if inMSet( c, n ) == True:
                image.plotPoint(col, row)
    # we looped through every image pixel; we now write the file
    image.saveFile()

mset()