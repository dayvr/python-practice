# Pascal's Triangle
#                    1
#                   1 1
#                  1 2 1
#                 1 3 3 1
#                1 4 6 4 1
#                  
# Each number is the sum of the number above it to the left and the number above
# it to the right (any missing numbers are counted as 0).

from UnitaryTest.test_tools import TestTools

def get_next_row(l):
    next_row = [1]
    for i in range(len(l)):
        next_num = sum(l[i:i+2])
        next_row.append(next_num)
    return next_row

# Takes a number n as input, and returns a list of the first n rows in the triangle. 
def triangle(n):
    if n == 0:
        return []
    if n == 1:
        return [[1]]
    else:
        result = triangle(n-1)
        next_row = get_next_row(result[-1])
        result.append(next_row)
    return result

# Non-recursive versions of previous function
def triangle_not_recursive(n):
    result = []
    for i in range(n):
        if i == 0:
            result.append([1])
            continue
        result.append(get_next_row(result[-1]))
    return result

def triangle_not_recursive_2(n):
    result = []
    prev = []
    for i in range(n):
        if i > 0:
            prev = result[-1]
        result.append(get_next_row(prev))
    return result

def main():
    t = TestTools()
    # Test triangle
    t.new_test(func=triangle)
    t.evaluate_result(triangle(0), expected=[])

    t.new_test(func=triangle)
    t.evaluate_result(triangle(1), expected=[[1]])

    t.new_test(func=triangle)
    t.evaluate_result(triangle(2), expected=[[1], [1, 1]])

    t.new_test(func=triangle)
    t.evaluate_result(triangle(3), expected=[[1], [1, 1], [1, 2, 1]])

    t.new_test(func=triangle)
    t.evaluate_result(triangle(6), expected=[[1], [1, 1], [1, 2, 1], 
                                            [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]])
    # Test triangle_not_recursive and triangle_not_recursive_2
    t.new_test(func=triangle_not_recursive)
    t.evaluate_result(triangle_not_recursive(6), expected=[[1], [1, 1], [1, 2, 1], 
                                            [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]])
    t.new_test(func=triangle_not_recursive_2)
    t.evaluate_result(triangle_not_recursive_2(6), expected=[[1], [1, 1], [1, 2, 1], 
                                            [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]])
    # Test get_row
    t.new_test(func=get_next_row)
    t.evaluate_result(get_next_row([1, 3, 3, 1]), expected=[1,4,6,4,1])

    t.new_test(func=get_next_row)
    t.evaluate_result(get_next_row([1, 5, 10, 10, 5, 1]), expected=[1,6,15,20,15,6,1])


if __name__ == '__main__':
    main()
