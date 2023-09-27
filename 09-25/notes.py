"""
mystery function:
takes input we are searching for and list
outputs true if in list, false if not

it uses the map function to tell if x is equal to an item in L
then takes the sum of all the true and false, true = 1, false = 0
so when sum is taken, if the sum is above 0, then there is at least 1 true
"""

def mystery(item, L):
    newL = map(lambda X : X == item, L)
    print(newL)
    newL = list(newL)
    #some how list changes what newL is, even if the memory address/pointer/or whatever is the same
    #ok so list(newL) creates a list, but newL is used up, which is why memory address stays the same
    #but if list(newL) is called again, there's nothing
    return sum(newL) > 0

item = 5
lst = [1, 3, 5, 12, 30]
print(f"Is {item} in the list: {lst}->", mystery(item, lst))


c = 50
it = [3, 10, 20, 100, 41]
#subset sum problems
#given capacity and list of positive number items, maximize sum without exceeding capacity
def subset(capacity, items):
    #if there is no capacity or there are no items, 0
    if capacity <= 0 or items == []:
        return 0
    #in case we want to filter out items over capacity
    # items = list(filter(lambda x : x <= capacity, items))
    elif items[0] > capacity:
        return subset(capacity, items[1:])
    else:
        use_it = items[0] + subset(capacity - items[0], items[1:])
        lose_it = subset(capacity, items[1:])
        return max(use_it, lose_it)

print(subset(c, it))

"""
(incomplete) trace for subset(7, [2, 3, 4])
better to actually do this on paper and write out a tree
capacity not less than or equal to 0, items not empty list
items[0] not > capacity
use_it = 2 + subset(5, [3,4])
->capacity not less than or equal to 0, items not empty
->items[0] not > capacity
->use_it = 3 + subset(2, [4])
--->capacity not less than or equal to 0, items not empty list
--->items[0] > capacity
--->subset(2, [])
----->empty list, return 0
--->2
->use_it = 5
->lose_it = subset(7, [3,4])
--->use_it = 3 + subset(4, [4])
----->use_it = 4 + subset(0, [])
------->0
----->4
--->7
lose_it

"""