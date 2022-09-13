from UnitaryTest.test_tools import TestTools

# Date Converter

english = {1:"January", 2:"February", 3:"March", 4:"April", 5:"May", 
6:"June", 7:"July", 8:"August", 9:"September",10:"October", 
11:"November", 12:"December"}
# then  "5/11/2012" is converted to "11 May 2012". 

# If the dictionary is in Swedish
swedish = {1:"januari", 2:"februari", 3:"mars", 4:"april", 5:"maj", 
6:"juni", 7:"juli", 8:"augusti", 9:"september",10:"oktober", 
11:"november", 12:"december"}
# then "5/11/2012" should be converted to "11 maj 2012".
# Hint: int('12') converts the string '12' to the integer 12.

# Takes two inputs. The first is a dictionary and the second a string. 
# The string is a valid date in the format month/day/year.
# Return the date written in the form <day> <name of month> <year>.
def date_converter(d, s):
    date = s.split('/')
    month = d[int(date[0])]
    day = date[1]
    year = date[2]
    return '{} {} {}'.format(day, month, year)

def date_converter_improved(language, date):
    month, day, year = date.split('/')
    return '{} {} {}'.format(day, language[int(month)], year)

def main():
    t = TestTools()

    t.new_test(func=date_converter)
    t.evaluate_result(date_converter(english, '5/11/2012'), expected='11 May 2012')  
    
    t.new_test(func=date_converter)
    t.evaluate_result(date_converter(english, '5/11/12'), expected='11 May 12')
    
    t.new_test(func=date_converter)
    t.evaluate_result(date_converter(swedish, '5/11/2012'), expected='11 maj 2012')

    t.new_test(func=date_converter)
    t.evaluate_result(date_converter(swedish, '12/5/1791'), expected='5 december 1791')

    t.new_test(func=date_converter_improved)
    t.evaluate_result(date_converter_improved(swedish, '12/5/1791'), expected='5 december 1791')

if __name__ == '__main__':
    main()
