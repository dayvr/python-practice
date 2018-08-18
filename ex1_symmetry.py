from UnitaryTest.test import evaluate_result

def getCol(L, pos):
    column = []
    for i in range(len(L)):
        column.append(L[i][pos])         
    return column

def comparing(row, col):
    return row == col

def symmetric(L):
    symmetric = True
    for i in range(len(L)):
        row = L[i]
        col = getCol(L, i)
        symmetric = comparing(row, col)
        if not symmetric:
            break
    return symmetric

def main():
    nS = [[1,2,3],[4,5,6],[7,8,9]]
    s = [[1, 2, 3], [2, 3, 4], [3, 4, 1]]
    nS_2 = [["cat", "dog", "fish"],
            ["dog", "dog", "dog"],
            ["fish","fish","cat"]]
    nS_3 = []
    
    # GetCol Test
    print('result1: {}'.format(evaluate_result(getCol(s, 2), expected=[3,4,1])))
    
    # Symmetric test
    print('result2: {}'.format(evaluate_result(symmetric(s), expected=True)))
    print('result3: {}'.format(evaluate_result(symmetric(nS), expected=False)))
    print('result4: {}'.format(evaluate_result(symmetric(nS_2), expected=False)))
    print('result5: {}'.format(evaluate_result(symmetric(nS_3), expected=True)))

    # Comparing tests
    print('result6: {}'.format(evaluate_result(comparing([1,2,3], [1,2,4]), expected=False)))


if __name__ == "__main__":
    main()