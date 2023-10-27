#intro to boolean logic and logic gates

"""
not:
x NOT x
0 1
1 0
gives opposite
not x written as x with bar over, but since I can't do bars over chars, I use !

and:
x y | x AND y
0 0 | 0
0 1 | 0
1 0 | 0
1 1 | 1
can be written xy (multiplication)
(carry in addition)

or:
x y | x OR y
0 0 | 0
0 1 | 1
1 0 | 1
1 1 | 1
can be written x + y

xor (exclusive or) logic table:
x y f(x, y)
0 0 0
0 1 1 !xy
1 0 1 x!y
1 1 0
x ^ y in python, 1 bit adder

multiplication is and
+ is or

minterm expansion principle
- find lines where output = 1
- negate the variables which are 0
(xnor gate, but how to build using and, not, or gates?)
x y | output
0 0 | 1 !x!y = 1
1 0 | 0 
0 1 | 0 
1 1 | 1 xy = 1
!x!y + xy
from this, we can draw circuit (in another file in same directory)

but now if we have 3 inputs, x, y, z
(odd parity circuit, odd number of 1s)
x y z | output
0 0 0 | 0
0 0 1 | 1 !x!yz
0 1 0 | 1 !xy!z
0 1 1 | 0
1 0 0 | 1 x!y!z
1 0 1 | 0
1 1 0 | 0
1 1 1 | 1 xyz
- find minterms, where output is 0, negate the 0s in the input
!x!yz + !xy!z + x!y!z + xyz (long formula)
!x(!yz + y!z) + x(!y!z + yz) (technically we could use xor gates, but only use and, or, not gates)
first one is y xor z, second is y xor z negated (xnor)

addition done using "full adder"
x y carryin | sum carryout
0 0 0 | 0 0 
0 0 1 | 1 0
0 1 0 | 1 0
0 1 1 | 0 1 !xy(cin)
1 0 0 | 1 0
1 0 1 | 0 1 x!y(cin)
1 1 0 | 0 1 xy(!cin)
1 1 1 | 1 1 xy(cin)
here, sum is odd parity circuit, carryout is when there is at least 2 1s
!xy(cin) + x!y(cin) + xy(!cin) + xy(cin)
ycin(!x + x) + x(!ycin + y(!cin)) (second one is xor) (first one is always 1)
ycin + x(!ycin + y(!cin))
"""