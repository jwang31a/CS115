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