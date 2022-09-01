# The Fibonacci sequence is obtained by adding the previous two consecutive terms
#
# Two Base Cases: fibonacci(0) => 0 ; fibonacci(1) => 1
# Recursive Case:
#                n > 1 : fibonacci(n) => fibonacci(n-1) + fibonacci(n-2)
#
###############################################################################################################
#
# The first and second terms of the Fibonacci sequence are 0 and 1 respectively. 
# Each successive term in the sequence is then calculated by adding the two preceding terms. 
# That is, the nth term is calculated by adding the (n-2)th and (n-1)th terms. 
# Thus, store the already computed sequence in a list to be able to calculate each new element in the sequence.
def fibonacci(n):
  myArray = []
  for i in range(n):
    if i is 0 or i is 1:
      myArray.append(i)
      yield i
    else:
      x = myArray[i-2] + myArray[i-1]
      myArray.append(x)
      yield x
      
for i in fibonacci(8):
  print(i)

from UnitaryTest.test_tools import TestTools

# Faster fibonacci function
def faster_fibonacci(n):
    current, after = 0, 1
    for _ in range(n):
        current, after = after, current + after # a, b = b, a+b
    return current

# Function that takes a natural number as its input, and returns the value of that fibonacci number.
def fibonacci(n):
    if n <= 1:
        return n
    else:
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
