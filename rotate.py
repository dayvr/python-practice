
from ex20_shift import shift_n_letters
from UnitaryTest.test_tools import TestTools

# Takes as its input a string of lower case letters, a-z, and spaces, and an integer n, 
# and returns the string constructed by shifting each of the letters n steps, and leaving 
# the spaces unchanged.
def rotate(words, n):
    output = []
    for i in words:
        if i == ' ':
            output.append(i)
        else:
            shifted = shift_n_letters(i, n)
            output.append(shifted)
    return ''.join(output)
 
# One-liner version
def rotate_improved(string, n):
    return ''.join([chr(((ord(i)-97+n)%26)+97) if i != ' ' else ' ' for i in string])

def main():
    t = TestTools()
    
    t.new_test('test 1-->rotate')
    t.evaluate_result(rotate('sarah', 13), expected='fnenu')

    t.new_test('test 2-->rotate')
    t.evaluate_result(rotate('fnenu', 13), expected='sarah')
    
    t.new_test('test 3-->rotate')
    t.evaluate_result(rotate('dave', 5), expected='ifaj')
    
    t.new_test('test 4-->rotate')
    t.evaluate_result(rotate('ifaj',-5), expected='dave')
    
    t.new_test('test 5-->rotate')
    t.evaluate_result(rotate("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu sv rscv kf ivru kyzj",-17), 
    expected='if your code works correctly you should be able to read this')
    
    t.new_test('test 6-->rotate')
    t.evaluate_result(rotate('this course teaches you to code', 7), 
    expected='aopz jvbyzl alhjolz fvb av jvkl')
    

if __name__ == '__main__':
    main()
