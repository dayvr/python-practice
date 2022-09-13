from UnitaryTest.test_tools import TestTools

# Longest Repetition

def eval_key(key_str):
    try:
        key = eval(key_str)
    except:
        key = key_str
    return key

def get_max(d, l):
    max_value = None
    max_key = None
    for i in l:
        value = d[str(i)]
        if not max_value or value > max_value:
            max_key = i
            max_value = value
    return max_key

def create_dict(l):
    rept = {}
    prev = None
    count = 0
    for i in l:
        if not prev:
            prev = i
        if i != prev:
            rept[str(prev)] = count
            count = 0
            prev = i
        count += 1
    rept[str(prev)] = count
    return rept

# Takes as input a list, and returns the element in the list that has the most 
# consecutive repetitions. If there are multiple elements that 
# have the same number of longest repetitions, the result should 
# be the one that appears first. If the input list is empty, 
# it returns None.
def longest_repetition(l):
    count = create_dict(l)
    key = get_max(count, l)
    return key

# A shorter versions of the above functions
def get_max_pythonic(d):
    if not d:
        return None
    return sorted(d.items(), key=lambda x: x[1], reverse=True)[0][0]

def longest_repetition_pythonic(l):
    count = create_dict(l)
    key = eval_key(get_max_pythonic(count))
    return key
            
def main():
    t = TestTools()

    t.new_test(func=longest_repetition)
    t.evaluate_result(longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1]), expected=3)

    t.new_test(func=longest_repetition)
    t.evaluate_result(longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd']), expected='b')

    t.new_test(func=longest_repetition)
    t.evaluate_result(longest_repetition([1,2,3,4,5]), expected=1)

    t.new_test(func=longest_repetition)
    t.evaluate_result(longest_repetition([]), expected=None)

    t.new_test(func=longest_repetition)
    t.evaluate_result(longest_repetition([[1], [2, 2], [2, 2], [2, 2], [3, 3, 3]]), expected=[2, 2])

    t.new_test(func=longest_repetition)
    t.evaluate_result(longest_repetition([2, 2, 3, 3, 3]), expected=3)

    t.new_test(func=longest_repetition)
    t.evaluate_result(longest_repetition([2, 2, 2, 3, 3, 3]), expected=2)

    # Tests pythonic functions
    t.new_test(func=longest_repetition_pythonic)
    t.evaluate_result(longest_repetition_pythonic([1, 2, 2, 3, 3, 3, 2, 2, 1]), expected=3)

    t.new_test(func=longest_repetition_pythonic)
    t.evaluate_result(longest_repetition_pythonic(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd']), expected='b')

    t.new_test(func=longest_repetition_pythonic)
    t.evaluate_result(longest_repetition_pythonic([1,2,3,4,5]), expected=1)

    t.new_test(func=longest_repetition_pythonic)
    t.evaluate_result(longest_repetition_pythonic([]), expected=None)

    t.new_test(func=longest_repetition_pythonic)
    t.evaluate_result(longest_repetition_pythonic([[1], [2, 2], [2, 2], [2, 2], [3, 3, 3]]), expected=[2, 2])

    t.new_test(func=longest_repetition_pythonic)
    t.evaluate_result(longest_repetition_pythonic([2, 2, 3, 3, 3]), expected=3)

    t.new_test(func=longest_repetition_pythonic)
    t.evaluate_result(longest_repetition_pythonic([2, 2, 2, 3, 3, 3]), expected=2)

    # Tests create_dict
    t.new_test(func=create_dict)
    t.evaluate_result(create_dict([1, 2, 2, 3, 3, 3, 2, 2, 1]), expected={'1': 1, '2': 2, '3': 3})



    

if __name__ == '__main__':
    main()
