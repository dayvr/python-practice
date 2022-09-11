# Family Trees
# Finds someone's ancestors, given a Dictionary that provides the parent relationships.  

from UnitaryTest.test_tools import TestTools

ada_family = { 'Judith Blunt-Lytton': ['Anne Isabella Blunt', 'Wilfrid Scawen Blunt'],
              'Ada King-Milbanke': ['Ralph King-Milbanke', 'Fanny Heriot'],
              'Ralph King-Milbanke': ['Augusta Ada King', 'William King-Noel'],
              'Anne Isabella Blunt': ['Augusta Ada King', 'William King-Noel'],
              'Byron King-Noel': ['Augusta Ada King', 'William King-Noel'],
              'Augusta Ada King': ['Anne Isabella Milbanke', 'George Gordon Byron'],
              'George Gordon Byron': ['Catherine Gordon', 'Captain John Byron'],
              'John Byron': ['Vice-Admiral John Byron', 'Sophia Trevannion'] }

# Takes as its first input a Dictionary in the form given above, and as its second input the name of a
# person. Return a list giving all the known ancestors of the input person (this should be the empty list if there are none). 
# The order of the list does not matter and duplicates will be ignored.

def ancestors(genealogy, person):
    if person in genealogy:
        parents = genealogy[person]
        result = parents
        for parent in parents:
            result = result + ancestors(genealogy, parent)
        return result
    return []

def main():
    t = TestTools()

    t.new_test(func=ancestors)
    t.evaluate_result(ancestors(ada_family, 'Augusta Ada King'), 
                                                        expected=['Anne Isabella Milbanke', 
                                                                  'George Gordon Byron','Catherine Gordon',
                                                                  'Captain John Byron'])

    t.new_test(func=ancestors)
    t.evaluate_result(ancestors(ada_family, 'Judith Blunt-Lytton'), 
                                                        expected=['Anne Isabella Blunt', 
                                                                  'Wilfrid Scawen Blunt', 'Augusta Ada King',
                                                                  'William King-Noel', 'Anne Isabella Milbanke', 
                                                                  'George Gordon Byron',
                                                                  'Catherine Gordon', 'Captain John Byron'])

    t.new_test(func=ancestors)
    t.evaluate_result(ancestors(ada_family, 'Dave'), expected=[])

if __name__ == '__main__':
    main()
