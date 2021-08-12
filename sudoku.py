sudoku = [[8,3,9,5,7,2,1,4,6],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0]]

def printSudoku():

    for i in sudoku:
        for j in i:
            print("\t"+str(j),end="")
        print("\n")
        
    print("\n")

def checkSudoku(row,column,num):
    
    for x in range(9):
        if sudoku[row][x]==num:
            return False
        
    for x in range(9):
        if sudoku[x][column]==num:
            return False
    
    startRow = row - row%3
    startColumn = column - column%3
    for i in range(3):
        for j in range(3):
            if sudoku[i+startRow][j+startColumn]==num:
                return False
    
    return True
        
def solSudoku(row,column):
    
    if row==8 and column==9:
        return True
    
    if column==9:
        row+=1
        column=0
        
    if sudoku[row][column]>0:
        return solSudoku(row,column+1)
    
    for num in range(9):
        if checkSudoku(row,column,num+1):       
            sudoku[row][column]=num+1
            if solSudoku(row,column+1):
                return True
        sudoku[row][column]=0
        
    return False
    
printSudoku()
solSudoku(0,0)
print("\n\nAfter Solution - \n")
printSudoku()
