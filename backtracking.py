"""
Problem Objectives:
given a number n "number of queens" on an n x n chessboard return all distinct solutions such that no 2 queens can attack each other.
Q = Queen , . = Empty "For Now"
logistices used : 
1 - placement of win in terms of 1d array which is nothing but the column num, 
for example let n= 4, the board takes values of [1,2,3,4] and they represents the column number for the Queen placement ,
the row or implement implied as 0,1,2,3 let's expand for better understanding:
Q . . . at row 0 column 0 a queen is placed
. Q . . at row 1 column 1 a queen is placed
. . Q . at row 2 column 2 a queen is placed
. . . Q at row 3 column 3 a queen is placed
another example where board takes numbers as [1,3,0,2]
. Q . . at row 0 column 1 a queen is placed 
. . . Q at row 1 column 3 a queen is placed
Q . . . at row 2 column 0 a queen is placed
. . Q . at row 3 column 2 a queen is placed
we will be using a 1d array to represent the queen placement why? because it's most optimized compared to 2d array
2 - Validating the queen replacement
we will be moving row after row so we have to consider 2 conditions to validate the queen placement :
a = no queen in same column
logic --> board[row] == j where row in range(i)
b = no queen in upper left diagonally
logic --> i-row == board[row]-j where row in range(i)
using DFS algorithm - Backtracking "Recusrive Algorithm"
"""
n = int(input("n-queens : "))

board = [-1] * n

def isvalid(i,j):
    for row in range(i):
        if board[row] == j or abs(row-i) == abs(board[row]-j):
            return False
    return True

def dfs(i, current_values):
    if i == n:
        for row in current_values:
            print(" ".join(row))
        return True
    for j in range(n):
        if isvalid(i,j):
            board[i] = j
            if dfs(i+1, current_values + ["."*j + "Q" + "." * (n-j-1)]):
                return True
    return False

dfs(0, [])

