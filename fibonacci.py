# Fibonacci series: the sum of two elements define the next
#
# Function that takes a natural number as its input, and
# returns the value of that fibonacci number.
#
# Two Base Cases: fibonacci(0) => 0 ; fibonacci(1) => 1
# Recursive Case:
#                n > 1 : fibonacci(n) => fibonacci(n-1) + fibonacci(n-2)
#
###############################################################################

from UnitaryTest.test_tools import TestTools

# Faster fibonacci function
def faster_fibonacci(n):
    current, after = 0, 1
    for _ in range(n):
        current, after = after, current + after
    return current

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

def main():
    t = TestTools()

    # Test fibonacci()
    t.new_test(func=fibonacci)
    t.evaluate_result(fibonacci(0), expected=0)

    t.new_test(func=fibonacci)
    t.evaluate_result(fibonacci(1), expected=1)

    t.new_test(func=fibonacci)
    t.evaluate_result(fibonacci(15), expected=610)

    # Test faster_fibonacci()
    t.new_test(func=faster_fibonacci)
    t.evaluate_result(faster_fibonacci(36), expected=14930352)

if __name__ == '__main__':
    main()
