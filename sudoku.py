def canbe(sud,row,column,x):
    for i in range(9):
        rtemp = 3*int(row/3) + int(i/3)
        ctemp = 3*int(column/3) + int(i%3)
        if sud[i][column]==x:
            return False
        elif sud[row][i] ==x:
            return False
        elif sud[rtemp][ctemp] ==x:
            return False
    return True

def solver(sud):
    for i in range(9):
        for j in range(9):
            if sud[i][j] == 0:
                for k in range(1,10):
                    if canbe(sud,i,j,k) == True:
                        sud[i][j] = k
                        if solver(sud) ==True:
                            return True
                        else:
                            sud[i][j] = 0
                return False
    return True

grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]

solver(grid)
for i in grid:
    print(i)