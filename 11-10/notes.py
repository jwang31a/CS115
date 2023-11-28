"""
largest signed 16 bit int is 2^15 - 1
(int starts with 2^0 and goes up to 2^15 bit, but the leftmost bit is a sign bit)

UTF stands for unicode transformation format
number that comes after is the bits

code creates variable, variables stored in heap
values of all objects stored in heap
(this heap is not the same as heap data structure)
stack and heap ram
values stored in different memory addresses (and if a variable uses a data type that is larger than the max storage of mem address, it'll be split)

python uses references in the stack to point to variables elsewhere (pointers)
but if a variable (like a string) holds multiple items, then how do we know to read multiple locations?
uses design: pointer points to another location that holds binary code for string of length 7
(not important in this course)

we will use box and arrow diagrams instead
variable name is one box, arrow points from that box to other boxes which contain the actual value
each box represents memory space, so when reassigning value of variable, old value isn't overwritten
garbage collector sees that old value is no longer used (referenced) and frees up memory
(some languages do not have garbage collection and freeing up memory is manual)


"""

x = 42
print("x's id: " + str(id(x)))
a = x
x = 43
print("x's new id: " + str(id(x)))
print("a's id: " + str(id(a)))
"""
x points to 42, a points to the value that x points to (which is 42)
so, a points to 42
when x changes to 43, a still points to the original value
(since a is not a pointer to x)
this is demonstrated by seeing that x's original id and a's new id are both the same
whenever a variable's value changes, it will be assigned a different mem address

if there's a list of values, the variable name points to more boxes that point to the actual value
when the value at an index is reassigned, the pointer changes somewhere else, old value stays where it is (until garbage collection)
if variable is assigned value of a list, the both point to the same list, so changes from one list will be reflected in the other list
(they are really the same list)
"shallow copy", elements not copied, pointers both refer to same thing
"""

w = [1,2,3,4]
z = w
w[2] = -100
print(z[2])
z[1] = 1212
print(w[1])