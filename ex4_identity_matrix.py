# By Ashwath from forums
# Given a list of lists representing a n * n matrix as input, 
# define a  procedure that returns True if the input is an identity matrix 
# and False otherwise.

# An IDENTITY matrix is a square matrix in which all the elements 
# on the principal/main diagonal are 1 and all the elements outside 
# the principal diagonal are 0. 
# (A square matrix is a matrix in which the number of rows 
# is equal to the number of columns)

from UnitaryTest.test import evaluate_result

def check_sz_row(row, size):
    res = True
    if len(row) != size:
        res = False
    return res

def check_id_row(row, pos):
    valid = True
    for i in range(len(row)):
        if i == pos:
            if row[i] != 1:
                valid = False
                break
        else:
            if row[i] != 0:
                valid = False
    return valid    

def is_identity_matrix(matrix):
    n = len(matrix)
    i = 0
    it_is_id = True
    it_is_sz = True
    while i < n and it_is_id and it_is_sz:
        it_is_sz = check_sz_row(matrix[i], n)
        it_is_id = check_id_row(matrix[i], i)
        i += 1
    return it_is_id and it_is_sz

def main():
    matrix1 = [[1,0,0,0],
               [0,1,0,0],
               [0,0,1,0],
               [0,0,0,1]]

    matrix2 = [[1,0,0],
               [0,1,0],
               [0,0,0]]

    matrix3 = [[2,0,0],
               [0,2,0],
               [0,0,2]]

    matrix4 = [[1,0,0,0],
               [0,1,1,0],
               [0,0,0,1]]

    matrix5 = [[1,0,0,0,0,0,0,0,0]]

    matrix6 = [[1,0,0,0],  
               [0,1,0,1],  
               [0,0,1,0],  
               [0,0,0,1]]

    matrix7 = [[1, -1, 1],
               [0, 1, 0],
               [0, 0, 1]]

    print('matrix 1: {}'.format(evaluate_result(is_identity_matrix(matrix1), expected= True)))
    print('matrix 2: {}'.format(evaluate_result(is_identity_matrix(matrix2), expected= False)))
    print('matrix 3: {}'.format(evaluate_result(is_identity_matrix(matrix3), expected= False)))
    print('matrix 4: {}'.format(evaluate_result(is_identity_matrix(matrix4), expected= False)))
    print('matrix 5: {}'.format(evaluate_result(is_identity_matrix(matrix5), expected= False)))
    print('matrix 6: {}'.format(evaluate_result(is_identity_matrix(matrix6), expected= False)))
    print('matrix 7: {}'.format(evaluate_result(is_identity_matrix(matrix7), expected= False)))

if __name__ == '__main__':
    main()