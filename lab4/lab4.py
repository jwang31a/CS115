"""
Jun Hong Wang
Lab 4: Knapsack Problem
10/5/23
I pledge my honor that I have abided by the Stevens Honor System.
"""

import sys

#this may not be needed
sys.setrecursionlimit(1000)


def knapsack(capacity, itemList):
    """
    knapsack takes an integer capacity and a 2d list of items
    every index of the list is a list with weight and value
    returns a list with index 0 being the maximum value, and the 1st index being a list of items that maximizes value

    calls a helper function that gets a list of items that maximizes value
    then calculate value based on that list and return list
    """
    l = knapsackHelper(capacity, itemList)
    # print(l)
    val = sum(value(l))
    return [val, l]

def knapsackHelper(capacity, itemList):
    """
    takes in a capacity and list of items, returns the list of items that maximizes value
    chooses the list that has more value in the else statement
    """
    if itemList == []:
        # print("item list empty was reached")
        return []
    elif capacity == 0:
        # print("capacity was reached")
        return []
    elif itemList[0][0] > capacity:
        # print("item weight was reached")
        # print(capacity, itemList[0][0])
        return knapsackHelper(capacity, itemList[1:])
    else:
        use = [itemList[0]] + knapsackHelper(capacity - itemList[0][0], itemList[1:])
        lose = knapsackHelper(capacity, itemList[1:])
        use_value = sum(value(use))
        lose_value = sum(value(lose))
        if max(use_value, lose_value) == use_value:
            # print("use value was reached")
            return use
        else:
            # print("lose value was reached")
            return lose

def value(list):
    """
    goes through value part of itemList and puts them in 1D list
    """
    if list == [] or list == [[]]:
            return []
    else:
        return [list[0][1]] + value(list[1:])
    
def sum(l):
    """
    takes list of ints and sums them up
    """
    if l == []:
        return 0
    return l[0] + sum(l[1:])

# museumItems = [[1, 4], [5, 150], [4, 180]]
# capacity = 6

# print(knapsack(capacity, museumItems))
# knapsack(capacity, museumItems)

# knapsackHelper(25, [[36, 35], [10, 28], [39, 47], [8, 1], [7, 24]])
