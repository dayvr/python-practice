from UnitaryTest.test_tools import TestTools

# Deep Reverse

# Return True if p is a list and False if it is not.
def is_list(p):
    return isinstance(p, list)

# As input a list, returns a new list that is the deep reverse of the input list. 
# This means it reverses all the elements in the list, and if any of those elements 
# are lists themselves, reverses all the elements in the inner list, all the way down. 
def deep_reverse(l):
    rev = []
    for i in range(len(l)-1, -1, -1):
        if is_list(l[i]):
            val = deep_reverse(l[i])
        else:
            val = l[i]
        rev.append(val)
    return rev

def main():
    t = TestTools()
    
    m = [1, 2]
    t.new_test(func=deep_reverse)
    t.evaluate_result(deep_reverse(m), expected=[2, 1])

    n = [1, [2, 3]]
    t.new_test(func=deep_reverse)
    t.evaluate_result(deep_reverse(n), expected=[[3, 2], 1])
    
    o = [[1, 2], 3]
    t.new_test(func=deep_reverse)
    t.evaluate_result(deep_reverse(o), expected=[3, [2, 1]])

    p = [1, [2, 3, [4, [5, 6]]]]
    t.new_test(func=deep_reverse)
    t.evaluate_result(deep_reverse(p), expected=[[[[6, 5], 4], 3, 2], 1])

    q =  [1, [2,3], 4, [5,6]]
    t.new_test(func=deep_reverse)
    t.evaluate_result(deep_reverse(q), expected=[ [6,5], 4, [3, 2], 1])
    

if __name__ == '__main__':
        main()
