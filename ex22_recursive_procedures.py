# Define a procedure, factorial, that takes a natural number as its input, and
# returns the number of ways to arrange the input number of items.
###################################################################################
# Define a procedure is_palindrome, that takes as input a string, and returns a
# Boolean indicating if the input string is a palindrome.
# Base Case: '' => True
# Recursive Case: if first and last characters don't match => False
# if they do match, is the middle a palindrome?

from UnitaryTest.test_tools import TestTools

def is_palindrome_recursive(s):
    if len(s) < 2:
        return True
    return s[0] == s[-1] and is_palindrome_recursive(s[1:-1])

def is_palindrome(s):
    return s == s[::-1]
    
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

def main():
    t = TestTools()

    # Test factorial    
    t.new_test(func=factorial)
    t.evaluate_result(factorial(0), expected=1)
    
    t.new_test(func=factorial)
    t.evaluate_result(factorial(5), expected=120)

    t.new_test(func=factorial)
    t.evaluate_result(factorial(10), expected=3628800)

    # Test is_palindrome
    t.new_test(func=is_palindrome)    
    t.evaluate_result(is_palindrome(''), expected=True)

    t.new_test(func=is_palindrome)
    t.evaluate_result(is_palindrome('abab'), expected=False)

    t.new_test(func=is_palindrome)
    t.evaluate_result(is_palindrome('abba'), expected=True)

    t.new_test(func=is_palindrome_recursive)    
    t.evaluate_result(is_palindrome_recursive('abab'), expected=False)

    t.new_test(func=is_palindrome_recursive)    
    t.evaluate_result(is_palindrome_recursive('abba'), expected=True)

    t.new_test(func=is_palindrome_recursive)    
    t.evaluate_result(is_palindrome_recursive('acba'), expected=False)

    t.new_test(func=is_palindrome_recursive)    
    t.evaluate_result(is_palindrome_recursive('dbba'), expected=False)

if __name__ == '__main__':
    main()
