sudoku = [[8,3,9,5,7,2,1,4,6],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0]]

"""sudoku = [[0,7,0,0,0,9,0,4,0],
          [2,0,3,1,4,0,0,0,6],
          [0,0,0,0,0,0,0,3,0],
          [8,0,0,0,0,0,0,7,0],
          [0,1,0,5,6,2,0,9,0],
          [0,5,0,0,0,0,0,0,4],
          [0,4,0,0,0,0,0,0,0],
          [7,0,0,0,2,4,8,0,1],
          [0,6,0,7,0,0,0,2,0]]"""


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



"""


fixed = [[0,1,0,0,0,1,0,1,0],
          [1,0,1,1,1,0,0,0,1],
          [0,0,0,0,0,0,0,1,0],
          [1,0,0,0,0,0,0,1,0],
          [0,1,0,1,1,1,0,1,0],
          [0,1,0,0,0,0,0,0,1],
          [0,1,0,0,0,0,0,0,0],
          [1,0,0,0,1,1,1,0,1],
          [0,1,0,1,0,0,0,1,0]]

def solSudoku(row,column):
    
    print(row,column)
    if fixed[row][column] == 1:
        if column!=8:
            solSudoku(row,column+1)
        elif row!=8:
            solSudoku(row+1,0)
        else:
            return 1
    else:    
        for i in range(9):
            print("Value = "+str(i+1))
            print("CheckRow = "+str(checkRow(row,column,i+1)))
            print("CheckCol = "+str(checkColumn(row,column,i+1)))
            print("CheckCube = "+str(checkCube(row,column,i+1)))
            if(checkRow(row,column,i+1)==1 and checkColumn(row,column,i+1)==1 and checkCube(row,column,i+1)==1):
                sudoku[row][column] = i+1
                print("Again")
                if row==8 and column==8:
                    return 1
                elif column!=8:
                    return solSudoku(row,column+1)
                elif row!=8:
                    return solSudoku(row+1,0)
            elif(i+1==9):
                return



"""


