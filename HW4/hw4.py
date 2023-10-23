"""
Jun Hong Wang
10/22/23
CS115
I pledge my honor that I have abided by the Stevens Honor System.
"""

"""
sample pascal's triangle
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
[1, 5, 10, 10, 5, 1]
"""

memo = {}
def pascal_row(n, col = 0):
    """
    uses helper function which gets specific values of pascal's triangle
    recursively generates the row from left to right
    memoized for speed
    """
    # print("in row")
    if (n, col) in memo:
        return memo[(n, col)]
    if col == n:
        return [1]
    ret = [pascal_row_helper(n, col)] + pascal_row(n, col + 1)
    memo[(n, col)] = ret
    return ret

memo2 = {}
def pascal_row_helper(n, col):
    """
    when the column is 0, then we've reached the leftmost element of the row, so that should be 1
    when the row is 0, there is only 1 slot, index 0
    if the index is anything but 0, then return 0 (bc we're adding from outside of the triangle)
    get the values above the value we want (one left, one right), return their sum
    memoized for speed, especially since pascal_row(50) wasn't working
    """
    # print(n, col)
    if (n, col) in memo2:
        return memo2[(n, col)]
    if col == 0:
        memo2[(n, col)] = 1
        return 1
    elif n == 0:
        memo2[(n, col)] = 0
        return 0
    else:
        leftVal = pascal_row_helper(n - 1, col - 1)
        rightVal = pascal_row_helper(n - 1, col)
        memo2[(n, col)] = leftVal + rightVal
        return leftVal + rightVal

def pascal_triangle(n, row=0):
    """
    uses pascal_triangle function I already made and recursively generates row
    base case is row == n + 1, because when row == n, pascal_triangle(0 won't work)
    also row variable is default set to 0 for convenience
    """
    # print("in pascal triangle")
    if row == n + 1:
        return []
    return [pascal_row(row)] + pascal_triangle(n, row + 1)

def test_pascal_row():
    """
    5 of my own assert tests for pascal_row, print statement at end will go off only if all the statements are passed
    """
    assert pascal_row(0) == [1]
    assert pascal_row(1) == [1, 1]
    assert pascal_row(2) == [1, 2, 1]
    assert pascal_row(3) == [1, 3, 3, 1]
    assert pascal_row(4) == [1, 4, 6, 4, 1]
    print("passed all row test cases")

def test_pascal_triangle():
    """
    5 of my own assert tests for pascal_triangle, print statement at end will go off only if all the statements are passed
    """
    assert pascal_triangle(0) == [ [1] ]
    assert pascal_triangle(1) == [ [1], [1, 1] ]
    assert pascal_triangle(2) == [ [1], [1, 1], [1, 2, 1] ]
    assert pascal_triangle(3) == [ [1], [1, 1], [1, 2, 1], [1, 3, 3, 1] ]
    assert pascal_triangle(4) == [ [1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1] ]
    print("passed all triangle test cases")

# print(pascal_row_helper(4, 0))
# print(pascal_row_helper(4, 1))
# print(pascal_row_helper(4, 2))
# print(pascal_row_helper(4, 3))
# print(pascal_row_helper(4, 4))
# print("===============")
# print(pascal_row(0))
# print(pascal_row(1))
# print(pascal_row(2))
# print(pascal_row(3))
# print(pascal_row(4))
# print(pascal_row(5))
# # print(pascal_row(50))
# print(memo2)
# print("===============")
# print(pascal_triangle(0))
# print(pascal_triangle(1))
# print(pascal_triangle(2))
# print(pascal_triangle(3))
# print(pascal_triangle(4))
# print(pascal_triangle(5))
# print(pascal_triangle(6))
# print("===============")
test_pascal_row()
test_pascal_triangle()