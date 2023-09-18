#conditionals and lambda functions

from functools import reduce

#conditionals work with boolean values, True and False
print(3 == 1 + 2)
#no typeerror, but it returns false
print(42 == "spam")
#but this returns a typeerror, > doesn't work with different types?
#old python turned strings into ASCII codes and compared the resulting numbers
# print("spam" > 42)

#not matching types, but result is 42 (probably because True is equivalent to 1)
print(True + 41)
print(int(True))
#therefore False holds 0
print(2 ** False == True)
#this may not hold in other language

x = 6
if x < 10:
    print("Hey")
elif x > 3:
    print("Yay")
elif x == 6: 
    print("Wow")
else:
    print("Nay")

#elif can be used as many times as needed (but at some point just use switch statements)

#showcase of boolean shortcircuiting
def superSpecial(x):
    if x < 42:
        return "Small number"
    elif x == 42 or x % 42 == 0:
        return "Nice!"
    elif 41 <= x <= 43:
        return "So close!"
    else:
        return "Yuck"

print(superSpecial(42))

#lambda functions, expressions, anonymous functions, etc whatever
#can assign to variable to make it callable
increment = lambda x : x + 1
print(increment(5))
#handy when using higher order functions
print(list(map(lambda t : t * 3, [1, 2, 3])))
#yeah this is pretty similar to javascript but cleaner

print(reduce(lambda x, y : x * y, [1, 2, 3, 4]))