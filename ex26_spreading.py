# Spreading Udaciousness
#
# One of our modest goals is to teach everyone in the world to program and
# understand computer science. To estimate how long this will take we have
# developed a (very flawed!) model:
#
# Everyone answering this question will convince a number, spread, (input to 
# the model) of their friends to take the course next offering. This will 
# continue, so that all of the newly recruited students, as well as the original
# students, will convince spread of their
# friends to take the following offering of the course.
# recruited friends are unique, so there is no duplication among the newly
# recruited students. Define a procedure, hexes_to_udaciousness(n, spread,
# target), that takes three inputs: the starting number of Udacians, the spread
# rate (how many new friends each Udacian convinces to join each hexamester),
# and the target number, and outputs the number of hexamesters needed to reach 
# (or exceed) the target.
# For credit, your procedure must not use: while, for, or import math. 

from UnitaryTest.test_tools import TestTools

def hexes_to_udaciousness(n, spread, target):
    if n >= target:
        return 0
    else:
        return 1 + hexes_to_udaciousness(n * (1 + spread), spread, target)
    return


def main():
    t = TestTools()

    # 0 more needed, since n already exceeds target
    t.new_test(func=hexes_to_udaciousness)
    t.evaluate_result(hexes_to_udaciousness(100000, 2, 36230), expected=0)

    # after 1 hexamester, there will be 50000 + (50000 * 2) Udacians
    t.new_test(func=hexes_to_udaciousness)
    t.evaluate_result(hexes_to_udaciousness(50000, 2, 150000), expected=1) 

    # need to match or exceed the target
    t.new_test(func=hexes_to_udaciousness)
    t.evaluate_result(hexes_to_udaciousness(50000, 2, 150001), expected=2)

    # only 12 hexamesters (2 years) to world domination!
    t.new_test(func=hexes_to_udaciousness)
    t.evaluate_result(hexes_to_udaciousness(20000, 2, 7 * 10 ** 9), expected=12)

    # more friends means faster world domination!
    t.new_test(func=hexes_to_udaciousness)
    t.evaluate_result(hexes_to_udaciousness(15000, 3, 7 * 10 ** 9), expected=10)
    
if __name__ == '__main__':
    main()
