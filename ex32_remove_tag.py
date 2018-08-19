# Remove Tags

# When we add our words to the index, we don't really want to include
# html tags such as <body>, <head>, <table>, <a href="..."> and so on.

# Write a procedure, remove_tags, that takes as input a string and returns
# a list of words, in order, with the tags removed. Tags are defined to be
# strings surrounded by < >. Words are separated by whitespace or tags. 
# You may assume the input does not include any unclosed tags, that is,  
# there will be no '<' without a following '>'.
from UnitaryTest.test_tools import TestTools

def remove_tags_improved(s):
    start = s.find('<')
    while start != -1:
        end = s.find('>')
        s = s[:start] + ' ' + s[end+1:]
        start = s.find('<')
    return s.split()

def parse_initial_text(s, start):
    ret = []
    stop = s.find('<', start)
    if stop == -1:
        stop = len(s)
    ret.extend(s[start:stop].split())
    return stop + 1, ret

def remove_tags(s):
    output = []
    start = 0
    start, words = parse_initial_text(s, start)
    output.extend(words)
    while (True):
        start = s.find('>', start)
        if start == -1:
            break
        start += 1
        stop = s.find('<', start)
        if stop == -1:
            stop = len(s)
        phrase = s[start:stop]
        output.extend(phrase.split())
    return output

def main():
    t = TestTools()

    # Tests remove_tags function
    t.new_test(func=remove_tags)
    t.evaluate_result(remove_tags('''<h1>Title</h1><p>This is a
                        <a href="http://www.udacity.com">link</a>.<p>'''), 
                        expected=['Title','This','is','a','link','.'])

    t.new_test(func=remove_tags)
    t.evaluate_result(remove_tags('''<table cellpadding='3'>
                        <tr><td>Hello</td><td>World!</td></tr>
                        </table>'''), expected=['Hello','World!'])

    t.new_test(func=remove_tags)
    t.evaluate_result(remove_tags("<hello><goodbye>"), expected=[])

    t.new_test(func=remove_tags)
    t.evaluate_result(remove_tags("This is plain text."), expected=['This', 'is', 'plain', 'text.'])
    
    t.new_test(func=remove_tags)
    t.evaluate_result(remove_tags("This is in <i>italics</i>"), expected=['This', 'is', 'in', 'italics'])

    # Tests remove_tags_improved
    t.new_test(func=remove_tags_improved)
    t.evaluate_result(remove_tags_improved('''<h1>Title</h1><p>This is a
                        <a href="http://www.udacity.com">link</a>.<p>'''), 
                        expected=['Title','This','is','a','link','.'])

    t.new_test(func=remove_tags_improved)
    t.evaluate_result(remove_tags_improved('''<table cellpadding='3'>
                        <tr><td>Hello</td><td>World!</td></tr>
                        </table>'''), expected=['Hello','World!'])

    t.new_test(func=remove_tags_improved)
    t.evaluate_result(remove_tags_improved("<hello><goodbye>"), expected=[])

    t.new_test(func=remove_tags_improved)
    t.evaluate_result(remove_tags_improved("This is plain text."), expected=['This', 'is', 'plain', 'text.'])
    
    t.new_test(func=remove_tags_improved)
    t.evaluate_result(remove_tags_improved("This is in <i>italics</i>"), expected=['This', 'is', 'in', 'italics'])


if __name__ == '__main__':
    main()
    