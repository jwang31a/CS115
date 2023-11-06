
"""
today, review on test 2
last time: i think it was assembly?

cheat sheet allowed, 1 page

topics:
number systems
minterm expansion principle (may include writing code or drawing circuit)
dictionaries
1 tail recursion
memoization (testing a function may be included)
loops
5-7 questions in total

(tracing is not on the test, but it may be a good idea to do it anyways)

y !y | y + !y
0 1    1
1 0    1
so that means y + !y can be simplified to just 1

memoization: put intermediate result in dictionary and then return it
(good idea to put it at the end before returning, but for other situations, could put it in between lines, somewhere in the middle, depending on situation)

tail recursive functions: just because there is a variable set in the parameters doesn't mean the function is tail recursive
tail recursion means that all the calculation is done on the way instead of at the end

number systems:
find negative number in binary (with specified length and two's complement)
-28 in base 2 using 10 bits, two's complement
28 = 0000011100 = 16 + 8 + 4
one's complement = 1111100011
two's complement = 1111100100
0 + 0 + 4 + 0 + 0 + 32 + 64 + 128 + 256 - 512
=4 + 32 + 64 + 128 + 256 - 512
"""