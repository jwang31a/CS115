def fibonacci(n, a = 0, b = 1):
    if n == 0:
        return a
    if n == 1:
        return b
    else:
        return fibonacci(n - 1, a = b, b = b + a)
    
# for i in range(10):
#     print(fibonacci(i))

#this is also a tail recursion function, since there is no extra calculation on traceback
def isPalindrome(word):
    #could switch the order of the cases around to optimize?
    #this case right here doesn't need to be so strict, if the word is just one letter, then it's a palindrome
    if word == "":
        return True
    elif word[0] == word[-1]:
        return isPalindrome(word[1:-1])
    else:
        return False
    
# print(isPalindrome("racecar"))
# print(isPalindrome("not a palindrome"))
# print(isPalindrome("tacocat"))

"""
tuples and dictionaries! yay
"""

#tuple, this variable has all of these values
#different from a list, immutable
t = 1234, 4567, "hello"
print(t)
try:
    t[1] = True
except:
    print("can't do that bozo, tuples are immutable")

#tuples can be added
u = t + (12, 34, 56)
print(u)

#tuples can also be embedded or in a list
u = t, (12, 34, 56)
print(u)

#since the tuple is in a list and we're just replacing part of the list, it's possible
#we're not actually modifying the tuple
#but the moment that the items in the tuple are modified, error
l1 = [ (23, 34), (56, 78) ]
l1[0] = (45, 56)

#if we try to modify an index of a tuple, we can't
#but if we get into the list inside of the tuple, we can modify it
t1 = ( [34, 45], [67, 78] )
try:
    t1[0] = [56, 78]
except:
    print("can't do that one buckaroo")
t1[0][0] = 56

empty = ()
#tuple with a single item 
#CAREFUL WITH THIS BC THIS COULD BE ON TEST
x = "hello",
print(x)