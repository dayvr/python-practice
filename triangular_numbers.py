from UnitaryTest.test_tools import TestTools

# Triangular Numbers

# The triangular numbers are the numbers 1, 3, 6, 10, 15, 21, ...
# They are calculated as follows.

# 1
# 1 + 2 = 3
# 1 + 2 + 3 = 6
# 1 + 2 + 3 + 4 = 10
# 1 + 2 + 3 + 4 + 5 = 15

# Takes as its input a positive integer n and returns the nth triangular number.
def triangular(n):
    i = 0
    result = 0
    while i < n + 1:
        result += i
        i += 1
    return result

def main():
    t = TestTools()

    t.new_test(func=triangular)
    t.evaluate_result(triangular(1), expected=1)

    t.new_test(func=triangular)
    t.evaluate_result(triangular(3), expected=6) 

    t.new_test(func=triangular)
    t.evaluate_result(triangular(10), expected=55)

if __name__ == '__main__':
    main()
