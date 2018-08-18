# Write a procedure, shift, which takes as its input a lowercase letter,
# a-z and returns the next letter in the alphabet after it, with 'a' 
# following 'z'.
#-----------------------------------------------------------------------
# Write a procedure, shift_n_letters which takes as its input a lowercase
# letter, a-z, and an integer n, and returns the letter n steps in the
# alphabet after it. Note that 'a' follows 'z', and that n can be positive,
#negative or zero.

import string
from UnitaryTest.test import init_test, new_test, evaluate_result, finish_test

def shift_n_letters(letter, n):
    letter_index = ord(letter) - ord('a')
    shifted_index = (letter_index + n) % 26 
    return chr(ord('a') + shifted_index)

def shift_improved(letter):
    letter_idx = ord(letter) - ord('a')
    shifted = (letter_idx + 1) % 26
    return chr(ord('a') + shifted)

def shift(letter):
    alphabet = string.ascii_lowercase
    next_letter = ''
    for i in range(len(alphabet)):
        if alphabet[i] == letter and alphabet[i] != 'z':
            next_letter = alphabet[i+1]
            break
        if letter == 'z':
            next_letter = 'a'
            break
    return next_letter

def main():

    init_test()

    # Test shift
    new_test()
    print('shift test 1: {}'.format(evaluate_result(shift('a'), expected='b')))
    print('shift test 2: {}'.format(evaluate_result(shift('n'), expected='o')))
    print('shift test 3: {}'.format(evaluate_result(shift('z'), expected='a')))

    # Test shift_2
    new_test()
    print('shift_improved_1: {}'.format(evaluate_result(shift_improved('a'), expected='b')))
    print('shift_improved_2: {}'.format(evaluate_result(shift_improved('n'), expected='o')))
    print('shift_improved_3: {}'.format(evaluate_result(shift_improved('z'), expected='a')))

    # Test shift_n_letters
    new_test()
    print('shift_n_letters_t1: {}'.format(evaluate_result(shift_n_letters('s', 1), expected='t')))
    print('shift_n_letters_t2: {}'.format(evaluate_result(shift_n_letters('s', 2), expected='u')))
    print('shift_n_letters_t3: {}'.format(evaluate_result(shift_n_letters('s', 10), expected='c')))
    print('shift_n_letters_t4: {}'.format(evaluate_result(shift_n_letters('s', -10), expected='i')))

    finish_test()
    
if __name__ == '__main__':
    main()
