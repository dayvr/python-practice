# Dictionaries of Dictionaries (of Dictionaries)

from UnitaryTest.test import evaluate_result

courses = {
    'feb2012': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Peter C.'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian',
                           'assistant': 'Andy'}},
    'apr2012': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Sarah'},
                 'cs212': {'name': 'The Design of Computer Programs',
                           'teacher': 'Peter N.',
                           'assistant': 'Andy',
                           'prereq': 'cs101'},
                 'cs253': 
                {'name': 'Web Application Engineering - Building a Blog',
                           'teacher': 'Steve',
                           'prereq': 'cs101'},
                 'cs262': 
                {'name': 'Programming Languages - Building a Web Browser',
                           'teacher': 'Wes',
                           'assistant': 'Peter C.',
                           'prereq': 'cs101'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian'},
                 'cs387': {'name': 'Applied Cryptography',
                           'teacher': 'Dave'}},
    'jan2044': { 'cs001': {'name': 'Building a Quantum Holodeck',
                           'teacher': 'Dorina'},
                 'cs003': {'name': 'Programming a Robotic Robotics Teacher',
                           'teacher': 'Jasper'},
                     }
    }

# For looping through the keys in the dictionary, you can use:
#         for <key> in <dictionary>:
#                    <block>  

def courses_offered(courses, hexamester):
    res = []
    for c in courses[hexamester]:
        res.append(c)
    return res
 
# Returns True if the input course is offered in the input hexamester, and False otherwise.
def is_offered(courses, course, hexamester):
    courses_list = courses_offered(courses, hexamester)
    it_is = False
    for i in range(len(courses_list)):
        if courses_list[i] == course:
            it_is = True
    return it_is

def is_offered_2(courses, course, hexamester):
    return course in courses[hexamester]

# Takes a courses data structure and a string representing a class, and returns a list of strings
# representing the hexamesters when the input course is offered.
def when_offered(courses,course):
    result = []
    for i in courses:
        if course in courses[i]:
            result.append(i)
    return result

# Takes as input a courses structure and a person and returns a Dictionary that 
# describes all the courses the person is involved in.  A person is involved 
# in a course if they are a value for any property for the course.  The output 
# Dictionary have hexamesters as its keys, and each value a list of courses that 
# offered that hexamester.
def involved(courses, person):
    d = {}
    for i in courses:
        for j in courses[i]:
            if person in courses[i][j].values():
                if i in d:
                    d[i].append(j)
                else:
                    d[i] = [j]           
    return d


def main():
    # Test is_offered
    print('test is_offered 1: {}'.format(evaluate_result(is_offered(courses, 'cs101', 'apr2012'), expected=True)))
    print('test is_offered 2: {}'.format(evaluate_result(is_offered(courses, 'cs003', 'apr2012'), expected=False)))
    print('test is_offered 3: {}'.format(evaluate_result(is_offered(courses, 'cs001', 'jan2044'), expected=True)))
    print('test is_offered 4: {}'.format(evaluate_result(is_offered(courses, 'cs253', 'feb2012'), expected=False)))
    print('test is_offered 5: {}'.format(evaluate_result(is_offered_2(courses, 'cs253', 'feb2012'), expected=False)))

    # Test when_offered
    print('test when_offered 1: {}'.format(evaluate_result(when_offered (courses, 'cs101'), expected=['feb2012','apr2012'])))
    print('test when_offered 2: {}'.format(evaluate_result(when_offered(courses, 'bio893'), expected=[])))

    # Test involved
    exp1 = {'apr2012': ['cs101', 'cs387'], 'feb2012': ['cs101']}    
    print('test involved 1: {}'.format(evaluate_result(involved(courses, 'Dave'), expected=exp1)))
    exp2 = {'apr2012': ['cs262'], 'feb2012': ['cs101']}
    print('test involved 2: {}'.format(evaluate_result(involved(courses, 'Peter C.'), expected=exp2)))
    exp3 = {'jan2044': ['cs001']}   
    print('test involved 3: {}'.format(evaluate_result(involved(courses, 'Dorina'), expected=exp3)))
    print('test involved 4: {}'.format(evaluate_result(involved(courses,'Peter'), expected={})))
    print('test involved 5: {}'.format(evaluate_result(involved(courses,'Robotic'), expected={})))
    print('test involved 6: {}'.format(evaluate_result(involved(courses, ''), expected={})))

if __name__ == '__main__':
    main()
