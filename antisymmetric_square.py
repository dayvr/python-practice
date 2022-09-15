from UnitaryTest.test import evaluate_result

# By Dimitris_GR from forums in Udacity course.
# An nxn square is called antisymmetric if A[i][j]=-A[j][i] 
# for each i=0,1,...,n-1 and for each j=0,1,...,n-1.

def getCol(L, pos):
    column = []
    for i in range(len(L)):
        column.append(L[i][pos])         
    return column

def comparing(row, col):
    anti = True
    for i in range(len(row)):
        if row[i] != col[i] * -1:
            anti = False
            break
    return anti

def antisymmetric(L):
    antisymmetric = True
    for i in range(len(L)):
        row = L[i]
        col = getCol(L, i)
        antisymmetric = comparing(row, col)
        if not antisymmetric:
            break
    return antisymmetric

def main():

    print('case 1: {}'.format(evaluate_result(antisymmetric(
                       [[0, 1, 2], 
                        [-1, 0, 3], 
                        [-2, -3, 0]]), expected= True)))  

    print('case 2: {}'.format(evaluate_result(antisymmetric(
                       [[0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0]]), expected= True)))

    print('case 3: {}'.format(evaluate_result(antisymmetric(
                       [[0, 1, 2], 
                        [-1, 0, -2], 
                        [2, 2,  3]]), expected= False)))

    print('case 4: {}'.format(evaluate_result(antisymmetric(
                       [[1, 2, 5],
                        [0, 1, -9],
                        [0, 0, 1]]), expected= False)))


if __name__ == '__main__':
    main()
