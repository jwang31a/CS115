"""
Jun Hong Wang
10/22/23
CS115
I pledge my honor that I have abided by the Stevens Honor System.
"""

"""
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
    memoized for speed, especially since pascal_row(50) wasn't working
    """
    # print(n, col)
    if (n, col) in memo2:
        return memo2[(n, col)]
    if col == 0:
        return 1
    elif n == 0:
        return 0
    else:
        leftVal = pascal_row_helper(n - 1, col - 1)
        rightVal = pascal_row_helper(n - 1, col)
        memo2[(n, col)] = leftVal + rightVal
        return leftVal + rightVal

def pascal_triangle(n, row=0):
    # print("in pascal triangle")
    if row == n + 1:
        return []
    return [pascal_row(row)] + pascal_triangle(n, row + 1)

def test_pascal_row():
    assert pascal_row(0) == [1]
    assert pascal_row(1) == [1, 1]
    assert pascal_row(2) == [1, 2, 1]
    assert pascal_row(3) == [1, 3, 3, 1]
    assert pascal_row(4) == [1, 4, 6, 4, 1]
    print("passed all row test cases")

def test_pascal_triangle():
    assert pascal_triangle(0) == [ [1] ]
    assert pascal_triangle(1) == [ [1], [1, 1] ]
    assert pascal_triangle(2) == [ [1], [1, 1], [1, 2, 1] ]
    assert pascal_triangle(3) == [ [1], [1, 1], [1, 2, 1], [1, 3, 3, 1] ]
    assert pascal_triangle(4) == [ [1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1] ]
    print("passed all triangle test cases")

print(pascal_row_helper(4, 0))
print(pascal_row_helper(4, 1))
print(pascal_row_helper(4, 2))
print(pascal_row_helper(4, 3))
print(pascal_row_helper(4, 4))
print("===============")
print(pascal_row(0))
print(pascal_row(1))
print(pascal_row(2))
print(pascal_row(3))
print(pascal_row(4))
print(pascal_row(5))
# print(pascal_row(50))
print("===============")
print(pascal_triangle(0))
print(pascal_triangle(1))
print(pascal_triangle(2))
print(pascal_triangle(3))
print(pascal_triangle(4))
print(pascal_triangle(5))
print(pascal_triangle(6))
print("===============")
test_pascal_row()
test_pascal_triangle()