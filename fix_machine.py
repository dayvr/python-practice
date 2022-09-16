from UnitaryTest.test_tools import TestTools
# Exercise from Udacity course.
# Takes 2 string inputs and returns the 2nd input string as the output if all of its
# characters can be found in the 1st input string and "Give me
# something that's not useless next time." if it's impossible.
# Letters that are present in the 1st input string may be used
# as many times as necessary to create the 2nd string.

def fix_machine(debris, product):
    i = 0
    valid = True
    result = ''
    while i < len(product) and valid:
        if product[i] in debris:
            i += 1
        else:
            valid = False
    if not valid:
        result = "Give me something that's not useless next time."
    else:
        result = product
    return result
                
def main():
    t = TestTools()
    
    t.new_test(func=fix_machine)
    t.evaluate_result(fix_machine('UdaciousUdacitee', 'Udacity'), expected="Give me something that's not useless next time.")

    t.new_test(func=fix_machine)
    t.evaluate_result(fix_machine('buy me dat Unicorn', 'Udacity'), expected='Udacity')

    t.new_test(func=fix_machine)
    t.evaluate_result(fix_machine('AEIOU and sometimes y... c', 'Udacity'), expected='Udacity')

    t.new_test(func=fix_machine)
    t.evaluate_result(fix_machine('wsx0-=mttrhix', 't-shirt'), expected='t-shirt')

if __name__ == '__main__':
    main()
