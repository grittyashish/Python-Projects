import numpy as np
import math
#Stack is required for backtracking => Use the function stack
def display() :
    for i in range(9):
        for j in range(9):
            print(matrix[i][j],end=" ")
        print()

def solve() :
    i,j = nextpos()
    if i == -1 :
        return True

    for k in range(1,10) :
        if isPossible(i,j,k) :
            matrix[i][j] = k
            if solve() :
                return True
            matrix[i][j] = 0

    return False

def nextpos():
    for i in range(9) :
        for j in range(9) :
            if matrix[i][j] == 0 :
                return i,j
    return -1,-1

#Function to check if placement possible for number k
def isPossible(row,col,k):
    #Checking in the same row and column
    if all([matrix[row][i] != k for i in range(9)]) is not True :
        return False
    if all([matrix[i][col] != k for i in range(9)]) is not True :
        return False

    #Checking in the current square's diagonals
    row = int(row/3)*3
    col = int(col/3)*3
    return all([matrix[i][j] != k for i in range(row,row+3) for j in range(col,col+3)])

    return True #If all above conditions does not exist => placement possible

matrix = np.empty(shape = (9,9),dtype=int)
#def solve_helper(mat) :
#    matrix = mat

def module_helper():
    return matrix

if __name__ == '__main__' :
    print("Enter the maze (use 0 for empty cells) : ")
    row = []
    for i in range(10):
           row.append(input())
    for i,k in enumerate(row) :
        r = k.split()
        for j,l in enumerate(r) :
            matrix[i][j] = l

    print("The Sudoku Entered is : ")
    for i in range(9):
        for j in range(9):
            print(matrix[i][j],end=" ")
        print()
    print("Solving ....")
    if solve() :
        display()
    else :
        print("Solution Not Possible")
