#
# life.py - Game of Life lab
#
# Name: Jun Hong Wang
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
#

import sys
import random

def createOneRow(width):
    """Returns one row of zeros of width "width"...  
       You should use this in your
       createBoard(width, height) function."""
    row = []
    for col in range(width):
        row += [0]
    return row

def createBoard(width, height):
    """
    creates a board of with specific width and height
    height = # of rows,
    width = # of cols,
    """
    board = []
    for i in range(height):
        board += [createOneRow(width)]
    return board

def printBoard( A ):
    """ this function prints the 2d list-of-lists
    A without spaces (using sys.stdout.write)
    """
    for row in A:
        for col in row:
            sys.stdout.write( str(col) )
        sys.stdout.write( '\n' )

# print(createBoard(4, 5))
# print(createBoard(5, 3))

# A = createBoard(5, 3)
# B = createBoard(4, 5)

# printBoard(A)
# printBoard(B)

def diagonalize(width,height):
    """ creates an empty board and then modifies it
    so that it has a diagonal strip of "on" cells.
    """
    A = createBoard( width, height )
    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0
    return A

# A = diagonalize(7, 6)
# printBoard(A)

def innerCells(w, h):
    """
    creates a board where edges are all 0, insides are 1
    """
    A = createBoard(w, h)
    for row in range(1, h-1):
        for col in range(1, w-1):
            A[row][col] = 1
    return A

# printBoard(innerCells(5, 5))
# printBoard(innerCells(1, 1))

def randomCells(w, h):
    """
    uses the random library to choose between 0 and 1
    only iterates through center of board
    """
    A = createBoard(w, h)
    for row in range(1, h-1):
        for col in range(1, w-1):
            A[row][col] = random.choice([0, 1])
    return A

# printBoard(randomCells(10, 10))

def copy(A):
    """
    deep copies A
    can't use list(A) because that creates references to nested lists rather than the values in them
    so we have to get each individual list and deep copy those
    """
    B = []
    for row in range(len(A)):
        B += [list(A[row])]
    return B
    

# oldA = createBoard(2,2)
# printBoard(oldA)
# print("\n")
# newA = copy(oldA)
# printBoard(newA)
# print("\n")
# oldA[0][0] = 1
# printBoard(oldA)
# print("\n")
# printBoard(newA)

def innerReverse(A):
    """
    copies A and stores in B
    wherever B is 1, turn that into a 0
    wherever B is 0, turn that into a 1
    """
    B = copy(A)
    for row in range(1, len(B) - 1):
        for col in range(1, len(B[row]) - 1):
            B[row][col] = int(not B[row][col])
    return B

# A = randomCells(8, 8)
# printBoard(A)
# print("\n")
# printBoard(innerReverse(A))

def next_life_generation(A):
    """ makes a copy of A and then advanced one
    generation of Conway's game of life within
    the *inner cells* of that copy.
    The outer edge always stays 0.
    """
    newA = copy(A)
    for row in range(1, len(newA) - 1):
        for col in range(1, len(newA[row]) - 1):
            n = countNeighbors(row, col, A)
            if n < 2 and A[row][col] == 1:
                newA[row][col] = 0
            if n > 3 and A[row][col] == 1:
                newA[row][col] = 0
            if n == 3 and A[row][col] == 0:
                newA[row][col] = 1
    return newA


def countNeighbors(row, col, A):
    """
    returns neighbors of a cell
    cell can't be its own neighbor
    when comparing position, we need to compare the whole coordinate rather than the components separately
    """
    n = 0
    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            # if r != row and c != row:
            if A[r][c] == 1 and [r,c] != [row,col]:
                n += 1
    return n

# test = [
#     [0, 0, 0, 0, 0 ,0], 
#     [0, 1, 1, 0, 1, 0], 
#     [0, 0, 1, 0, 1, 0], 
#     [0, 1, 0, 0, 0, 0], 
#     [0, 0, 1, 1, 0, 0], 
#     [0, 0, 0, 0, 0 ,0], 
# ]

# print(countNeighbors(3, 2, test))
# print(countNeighbors(2, 2, test))

# A = [
#     [0,0,0,0,0],
#     [0,0,1,0,0],
#     [0,0,1,0,0],
#     [0,0,1,0,0],
#     [0,0,0,0,0]
# ]
# printBoard(A)
# print()
# A2 = next_life_generation(A)
# printBoard(A2)
# print()
# A3 = next_life_generation(A2)
# printBoard(A3)
# print()

# A = randomCells(10, 10)
# for i in range(10):
#     A = next_life_generation(A)
#     printBoard(A)
#     print()

"""
extra note: apparently lifegraphics doesn't like me working on a virtual ubuntu shell
so i have to use the normal command prompt to run it
"""