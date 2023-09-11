#lists (or arrays)
L = [1, 42, 3, 4]
print(L)

#can't add list and int, type error
try:
    L + 10
except:
    print("can't add list and int")

print(L + [10])
# L.append(10) # but this is unknown alien technology for intro
#problem is time loss for large function calls
L += [10]
#or 
# L = L + [10]
print(L)

#multiplying list by int will double the list
print(L * 2)

#lists with multiple types, including other lists
#polymorphic, can take many forms/structures = can have many types
M = [1, 1.0, "bob", True, [2, 4, 5]]
#list 0-indexed, same way as strings
# print(M[4][2])
#can also do negative indexing
print(M[-1])

#slicing, inclusive start, exclusive end
s = "helpcopyrightcreditslicense"
print(s[0:4])
print(s[4:13])
print(s[13:20])
print(s[20:len(s)])
#negative slicing, pretty much converts the negative index to positive equivalent
print(s[0:-2])
#with step, skip the step - 1 characters 
print(s[0:15:2])

#slicing but for lists
#1 is default increment, no skips
print(M[0:2:1])

N = [42, 3, 98, 37]
#since 1 is default increment, step is 1 but hidden
print(N[0:2:1])
print(N[0:2])
print(N[0:3:2])

#without end value, end defaults to length of list/string
print(N[1:])

#without beginning value = -1 converted into positive index, beginning defaults to 0
print(N[:-1])

#cringe notation
print(N[1:-2])

#negative step
print(N[3:0:-1])
#empty list
print(N[0:3:-1])
#goes the other direction, gives the whole list backwards
#easy list/string reverse for Python (other languages have other ways)
print(N[::-1])
#exactly the same as if no beginning and end index
print(N[3:-5:-1])

#no beginning, end, or step
print(N[::])

#higher order functions: use functions to produce results, like functions as an argument
#map, reduce, filter
#map will apply a function to every element of a sequence, return an object output

def dbl(x):
    return x * 2

print(map(dbl, [0, 1, 2, 3, 4])) #dbl function applied on every element in the list, but returns a map object
print(list(map(dbl, [0, 1, 2, 3, 4])))
#if input this list into dbl without map, just duplicates the list

#or create a loop
