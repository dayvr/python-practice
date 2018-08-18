# The mean of a set of numbers is the sum of the numbers divided by the
# number of numbers. Write a procedure, list_mean, which takes a list of numbers
# as its input and return the mean of the numbers in the list.

# Hint: You will need to work out how to make your division into decimal
# division instead of integer division. You get decimal division if any of
# the numbers involved are decimals.

from UnitaryTest.test import evaluate_result

def list_mean(n):
    result = 0
    i = 0
    while i < len(n):
        result += n[i]
        i += 1
    return result / len(n)

def main():
    print('case 1: {}'.format(evaluate_result(list_mean([1,2,3,4]), expected= 2.5)))
    print('case 2: {}'.format(evaluate_result(list_mean([1,3,4,5,2]), expected= 3.0)))
    print('case 3: {}'.format(evaluate_result(list_mean([2]), expected= 2.0)))


if __name__ == '__main__':
    main()

