# Stirling and Bell Numbers

# The number of ways of splitting n items in k non-empty sets is called
# the Stirling number, S(n,k), of the second kind. For example, the group 
# of people Dave, Sarah, Peter and Andy could be split into two groups in 
# the following ways.

# 1.   Dave, Sarah, Peter         Andy
# 2.   Dave, Sarah, Andy          Peter
# 3.   Dave, Andy, Peter          Sarah
# 4.   Sarah, Andy, Peter         Dave
# 5.   Dave, Sarah                Andy, Peter
# 6.   Dave, Andy                 Sarah, Peter
# 7.   Dave, Peter                Andy, Sarah  ------------------------------->  S(4,2) = 7

# If instead we split the group into one group, we have just one way to 
# do it.
# 1. Dave, Sarah, Peter, Andy ------------------------------------------------>  S(4,1) = 1

# or into four groups, there is just one way to do it as well
# 1. Dave        Sarah          Peter         Andy  -------------------------->  S(4,4) = 1

# If we try to split into more groups than we have people, there are no
# ways to do it.

# The formula for calculating the Stirling numbers is
#  S(n, k) = k*S(n-1, k) + S(n-1, k-1)
# Furthermore, the Bell number B(n) is the number of ways of splitting n 
# into any number of parts, that is,

# B(n) is the sum of S(n,k) for k =1,2, ... , n.

from UnitaryTest.test_tools import TestTools

# Takes as its inputs two positive integers of which the first is the 
# number of items and the second is the number of sets into which those 
# items will be split. 
def stirling(n, k):
    if k == 1 or n == k:
        return 1
    if n < k:
        return 0 
    return k * stirling(n-1, k) + stirling(n-1, k-1)    

# Takes as input a positive integer n and returns the Bell number B(n).
def bell(n):
    accumulator = 0
    for k in range(1, n+1):
        accumulator += stirling(n, k)
    return accumulator

def main():
    t = TestTools()

    # test_data[n][0] -> input n ; test_data[n][1] -> output n
    test_data1 = [[(1,1),1], [(2,1),1], [(2,2),1], [(2,3),0], [(3,1),1], [(3,2),3],
                 [(3,3),1], [(4,1),1], [(4,2),7], [(4,3),6], [(4,4),1], [(5,1),1],
                 [(5,2),15], [(5,3),25], [(5,4),10], [(5,5),1], [(20,15),452329200]]
    for i in test_data1:
        t.new_test(func=stirling)
        t.evaluate_result(stirling(*i[0]), expected=i[1])

    # Tests bell function
    test_data2 = [[1,1], [2,2], [3,5], [4,15], [5,52], [15,1382958545]]
    for i in test_data2:
        t.new_test(func=bell)
        t.evaluate_result(bell(i[0]), expected=i[1])

if __name__ == '__main__':
    main()
