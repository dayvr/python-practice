# Deep Count 

# The built-in len() operator outputs the number of top-level elements in a List,
# but not the total number of elements. 
# The goal here is to count the total number of elements in a list, including all of the inner lists.

from UnitaryTest.test_tools import TestTools

# Test if a value is a list. 
# It returns True if the input is a List, and returns False otherwise.
def is_list(p):
    return isinstance(p, list)

# Takes as input a list, and outputs the total number of elements in the list, 
# including all elements in lists that it contains.
def deep_count(p):
    count = 0
    for i in p:
        count += 1
        if is_list(i):
            count += deep_count(i)
            if i == []:
                count += 0
    return count

def main():
    t = TestTools()

    t.new_test(func=deep_count)   
    t.evaluate_result(deep_count([1, 2, 3]),expected=3)     

    # The empty list still counts as an element of the outer list
    t.new_test(func=deep_count)
    t.evaluate_result(deep_count([1, [], 3]), expected=3)
    
    t.new_test(func=deep_count)
    t.evaluate_result(deep_count([1, [1, 2, [3, 4]]]), expected=7)

    t.new_test(func=deep_count)
    t.evaluate_result(deep_count([[[[[[[[1, 2, 3]]]]]]]]), expected=10)

    t.new_test(func=deep_count)
    t.evaluate_result(deep_count([1, 3, 6, 10, 15, 21, [2, []]]), expected=9)
   
if __name__ == '__main__':
    main()
