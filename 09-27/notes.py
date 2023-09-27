#more subset sum stuff?

#cool stuff with recursion limit
# import sys

# sys.setrecursionlimit(11000)

# def recursionTest(n):
#     if n >= 10000:
#         return "it worked"
#     return recursionTest(n + 1)

# print(recursionTest(1))

"""
subset sum pseudocode:
if list is empty or current element is greater than capacity remaining or capacity is negative, return 0
case 1: use the current element, sum of current element and subset(capacity - current element, rest of list)
case 2: don't use current element, call subset(capacity, rest of list)
then return the larger of the two

trace could be linear or tree, whichever is easier or makes more sense
"""

#knapsack problem: maximize worth while considering capacity
"""
items is 2D array, where first element in each array is weight, second is value
goal is not to maximize weight, but value
"""
def knapsack(capacity, items):
    if len(items) == 0 or capacity <= 0:
        return 0
    #this elif is pretty much a lose_it case, since we can't use this anyway
    elif items[0][0] > capacity:
        return knapsack(capacity, items[1:])
    else:
        use_it = items[0][1] + knapsack(capacity - items[0][0], items[1:])
        lose_it = knapsack(capacity, items[1:])
        return max(use_it, lose_it)

#maximum value should be 1.5 million and 12 (dollars)
print(knapsack(20, [ [19, 2*10**5], [12, 10**5], [9, 1.5*10**6], [12, 700], [5, 12] ]))
