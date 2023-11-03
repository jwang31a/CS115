"""
Jun Hong Wang
11/2/23
Lab 8
I pledge my honor that I have abided by the Stevens Honor System.
"""

def mult(c, n):
    """
    multiplication without multiplication operator (using addition and loop)
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