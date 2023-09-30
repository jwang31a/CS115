"""
Jun Hong Wang
I pledge my honor that I have abided by the Stevens Honor System.
Lab 3: Use it or lose it
9/29/23
"""


def change(amount, coins):
    """
    input an amount/value and a list of coins
    base cases:
    -if the list of coins is empty, then it's impossible, return infinity
    -if the amount is 0, good, so return 0
    -if the amount is negative, return inf
    -else, 1 + recursive call of change(amount - the first coin, coins)
    -take the first coin out, call change with the rest of coin list
    - return the minimum
    keep using the first coin until you can't, then don't use that coin and choose the next coin
    then keep using first coin
    returns minimum number of coins needed to get that exact value
    """
    # print(amount)
    if (coins == [] and amount > 0) or amount < 0:
        return float("inf")
    elif amount == 0:
        return 0
    else:
        use_it = 1 + change(amount - coins[0], coins)
        # print(use_it)
        lose_it = change(amount, coins[1:])
        return min(use_it, lose_it)

#this should be 6
print(change(48, [1, 5, 10, 25, 50]))
# change(48, [1, 5, 10, 25, 50])
#should be 2
print(change(48, [1, 7, 24, 42]))