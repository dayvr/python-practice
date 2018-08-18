# Question 1: Pick One
#
# Define a procedure, pick_one, that takes three inputs: a Boolean 
# and two other values. If the first input is True, it should return 
# the second input. If the first input is False, it should return the 
# third input.
#
# For example, pick_one(True, 37, 'hello') should return 37, and
# pick_one(False, 37, 'hello') should return 'hello'.
from UnitaryTest.test_tools import TestTools

def pick_one(boolean, second_value, third_value):
    if boolean:
        return second_value
    return third_value


def main():
    t = TestTools()

    t.new_test(func=pick_one)
    t.evaluate_result(pick_one(True, 37, 'hello'), expected=37)

    t.new_test(func=pick_one)
    t.evaluate_result(pick_one(False, 37, 'hello'), expected='hello')

    t.new_test(func=pick_one)
    t.evaluate_result(pick_one(True, 'red pill', 'blue pill'), expected='red pill')

    t.new_test(func=pick_one)
    t.evaluate_result(pick_one(False, 'sunny', 'rainy'),expected='rainy')
    print("hello")
    
if __name__ == '__main__':
    main()
