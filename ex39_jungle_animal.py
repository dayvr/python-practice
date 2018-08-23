# You are in the middle of a jungle. 
# Suddenly you see an animal coming to you. 
# Here is what you should do if the animal is:

# zebra >> "Try to ride a zebra!"
# cheetah >> If you are faster than a cheetah: "Run!" 
#            If you are not: "Stay calm and wait!". 
#            The speed of a cheetah is 115 km/h.
# anything else >> "Introduce yourself!"

# Define a procedure, jungle_animal, 
# that takes as input a string and a number, 
# an animal and your speed (in km/h), 
# and prints out what to do.
from UnitaryTest.test_tools import TestTools

def jungle_animal(animal, my_speed):
    instruction = ''
    jungle_rules = ["Introduce yourself!", "Stay calm and wait!", "Run!", "Try to ride a zebra!"]
    
    if animal == 'zebra':
        instruction = jungle_rules[-1]
        
    elif animal == 'cheetah':
        if my_speed <= 115:
            instruction = jungle_rules[1]
        else:
            instruction = jungle_rules[2]
    else:
        instruction = jungle_rules[0]
    return instruction

def main():
    t = TestTools()

    t.new_test(func=jungle_animal)
    t.evaluate_result(jungle_animal('cheetah', 30), expected="Stay calm and wait!")

    t.new_test(func=jungle_animal)
    t.evaluate_result(jungle_animal('cheetah', 120), expected="Run!")


    t.new_test(func=jungle_animal)
    t.evaluate_result(jungle_animal('zebra', 15), expected="Try to ride a zebra!")

    t.new_test(func=jungle_animal)
    t.evaluate_result(jungle_animal('gorilla', 21), expected="Introduce yourself!")

if __name__ == '__main__':
    main()
