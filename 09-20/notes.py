#recursion

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return factorial(n-1) * n

def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)

#input is a positive integer
def tower(n):
    if n == 1:
        return 2
    return 2 ** tower(n - 1)

#without using built in len() function
def length(List):
    l = 0
    if List[0:1] == []:
        # print(List[0:1])
        return l
    l += 1 + length(List[0 : -1])
    return l

print("factorial prints")
print(factorial(4))
print(factorial(5))

print("fibonnaci prints")
#0, 1, 1, 2, 3, 5, 8, 13, 21
for i in range(1, 8):
    print(fib(i))

print("tower test")
print(tower(3))
print(tower(4))

print("recursive length")
print(length([5,4,3,2,1]))
print(length([6,5,4,3,2,1]))
print(length([5,4,3,2,1,0,-1,-2]))
print(length([]))






#least to greatest
def merge_sort(l):
    if len(l) == 1:
        return l
    elif len(l) == 1:
        return
    l1 = l[0:len(l)//2]
    l2 = l[len(l)//2:len(l)]
    l1 = merge_sort(l1)
    l2 = merge_sort(l2)
    sorted = merge(l1, l2)
    return sorted

#takes a sorted list and merges
def merge(l1, l2):
    sorted = []
    print(l1, l2)
    i = 0
    j = 0
    s = 0
    while i < len(l1) and j < len(l2):
        if l1[i] >= l2[j]:
            sorted[s] += l2[j]
            sorted += l2[j]
            j += 1
        else:
            sorted[s] = l1[i]
            sorted += l1[i]
            i += 1
        s += 1

    return sorted
    
print("merge sort test")
l = [10,7,8,4,9,2,3,5,6]
# print(l[0:len(l)/2])
# print(len(l)//2)
print(merge_sort([10,7,8,4,9,2,3,5,6]))