# The built-in <string>.split() procedure works okay, but fails to find all the words on a page
# because it only uses whitespace to split the string. To do better, we should also use punctuation
# marks to split the page into words.

def drop_empty(result):
    res = []
    for i in result:
        if i != '':
            res.append(i)
    return res

def custom_split(source, char):
    if char == ' ':
        result = source.split()
    else:
        result = source.split(char)
    #result = list(filter(lambda x: x != '', result))
    result = drop_empty(result)
    return result

# Takes two inputs: the string to split and a string containing
# all of the characters considered separators. Return a list of strings that break
# the source string up by the characters in the splitlist.
def split_string(source, splitlist):
    splited = []
    for i in splitlist:
        if not splited:
            splited = custom_split(source, i)
        else:
            temp = []
            for j in splited:
                temp += custom_split(j, i)
            splited = temp
    return splited


def main():

    out = split_string("This is a test-of the,string separation-code!", " ,!-")
    print(out)
    #>>> ['This', 'is', 'a', 'test', 'of', 'the', 'string', 'separation', 'code']

    out = split_string("After  the flood   ...  all the colors came out.", " .")
    print(out)
    #>>> ['After', 'the', 'flood', 'all', 'the', 'colors', 'came', 'out']

    out = split_string("First Name,Last Name,Street Address,City,State,Zip Code", ",")
    print(out)
    #>>>['First Name', 'Last Name', 'Street Address', 'City', 'State', 'Zip Code']

if __name__ == '__main__':
    main()
