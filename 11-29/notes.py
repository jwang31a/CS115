#notes tracing will be on exam

def loop1():
    total = 0
    for i in range(1, 10, 3):
        total += i
    print(total)

def loop2():
    i = 0
    count = 0
    while i < 15:
        for k in range(5, 8):
            count += k
        i == 3
        if i > 10:
            break

#loop 3 is on paper

#Now oop? in python
#floating point addition is a bruh moment

class Rational:
    def __init__(self, d, n):
        if d == 0:
            raise ZeroDivisionError("don't divide by zero please")
        else:
            self.numerator = n
            self.numerator = d

    def izZero(self):
        return self.numerator == 0