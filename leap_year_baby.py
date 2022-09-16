from UnitaryTest.test_tools import TestTools

# A leap year baby is a baby born on Feb 29, which occurs only on a leap year.
# A year that is a multiple of 4 is a leap year unless the year is
# divisible by 100 but not a multiple of 400 (so, 1900 is not a leap
# year but 2000 and 2004 are).

def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

# Returns True if the date is a leap day (Feb 29 in a valid leap year), False otherwise.
def is_leap_baby(day,month,year):
    is_leap = is_leap_year(year)
    leap_baby = False
    if day == 29 and month == 2 and is_leap == True:
        leap_baby = True
    return leap_baby


# The function 'output' prints one of two statements based on whether 
# the is_leap_baby function returned True or False.

def output(status,name):
    if status:
        print("%s is a leap year baby!" % name)
    else:
        print("%s is not a leap year baby!" % name)

def main():
    t = TestTools()

    # Tests is_leap_baby
    t.new_test(func=is_leap_baby)
    t.evaluate_result(is_leap_baby(29, 2, 1996), expected=True)

    t.new_test(func=is_leap_baby)
    t.evaluate_result(is_leap_baby(29, 2, 1900), expected=False)

    # Tests output
    t.new_test(func=output)
    t.evaluate_result(output(True, 'Calvin'), expected=None)
    #>>> "Calvin is a leap year baby!"

    t.new_test(func=output)
    t.evaluate_result(output(False, 'Garfield'), expected=None)
    #>>> "Garfield is not a leap year baby!"

if __name__ == '__main__':
    main()
