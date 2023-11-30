'''
Created on 11/28/2023
@author:   Jun Hong Wang
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 5 
'''

lucasMemo = {}
def fast_lucas(n):
    '''Returns the nth Lucas number using the memoization technique
    shown in class and lab. The Lucas numbers are as follows:
    [2, 1, 3, 4, 7, 11, ...]
    0th number is 2, first is 1, then everything else is sum of n-1 and n-2
    '''
    if n in lucasMemo:
        return lucasMemo[n]
    elif n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        lucas = fast_lucas(n - 1) + fast_lucas(n - 2)
        lucasMemo[n] = lucas
        return lucas

changeMemo = {}
def fast_change(amount, coins):
    '''Takes an amount and a list of coin denominations as input.
    Returns the number of coins required to total the given amount.
    Use memoization to improve performance.
    (only works for one coin list though, since coin list isn't memoized)
    '''
    if amount in changeMemo:
        return changeMemo[amount]
    if (coins == [] and amount > 0) or amount < 0:
        return float("inf")
    elif amount == 0:
        return 0
    else:
        use_it = 1 + fast_change(amount - coins[0], coins)
        # print(use_it)
        lose_it = fast_change(amount, coins[1:])
        less = min(use_it, lose_it)
        changeMemo[amount] = less
        return less

# If you did this correctly, the results should be nearly instantaneous.
print(fast_lucas(3))  # 4
print(fast_lucas(5))  # 11
print(fast_lucas(9))  # 76
print(fast_lucas(24))  # 103682
print(fast_lucas(40))  # 228826127
print(fast_lucas(50))  # 28143753123

print(fast_change(131, [1, 5, 10, 20, 50, 100])) 
print(fast_change(292, [1, 5, 10, 20, 50, 100]))
print(fast_change(673, [1, 5, 10, 20, 50, 100]))
print(fast_change(724, [1, 5, 10, 20, 50, 100]))
print(fast_change(888, [1, 5, 10, 20, 50, 100]))


