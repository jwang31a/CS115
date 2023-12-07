class Rational:
    """
    all classes in python must have self as argument, like this keyword in other languages
    __init__ is the constructor
    __ in front of attributes makes attribute private
    _ in front a variable is naming convention for internal use inside the class
    trailing _ used when you want to reserved keyword as variable name
    _ by itself (like for _ in range(5)) means the variable name is insignificant, sort of a placeholder
    accessors/getter methods
    mutator/setter methods
    __ in front and after method name makes it reserved
    """
    def __init__(self, n, d):
        if d == 0:
            raise ZeroDivisionError("Denominator cannot be zero!")
        else:
            self.__denominator = d
            self.__numerator = n

    def get_numerator(self):
        return self.__numerator
    
    def set_numerator(self, newn):
        self.__numerator == newn

    def isZero(self):
        return self.numerator == 0
    
    def add(self, other):
        newDenominator = self.denominator * other.denominator
        newNumerator = self.numerator * other.denominator + self.denominator * other.numerator
        return Rational(newNumerator, newDenominator)

    def __add__(self, other):
        newDenominator = self.denominator * other.denominator
        newNumerator = self.numerator * other.denominator + self.denominator * other.numerator
        return Rational(newNumerator, newDenominator)