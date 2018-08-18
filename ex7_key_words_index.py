# Define a procedure, add_to_index,
# that takes 3 inputs:

# - an index: [[<keyword>,[<url>,...]],...]
# - a keyword: String
# - a url: String

# If the keyword is already
# in the index, add the url
# to the list of urls associated
# with that keyword.

# If the keyword is not in the index,
# add an entry to the index: [keyword,[url]]
# Define a procedure, lookup,
# that takes two inputs:

# - an index
# - keyword

# The procedure should return a list
# of the urls associated
# with the keyword. If the keyword
# is not in the index, the procedure
# should return an empty list.


def lookup(index,keyword):
    result = []
    for i in index:
        if i[0] == keyword:
            result = i[1]
            break
    return result

def add_to_index(index,keyword,url):
    item = []
    found = False
    for i in index:
        if keyword == i[0]:
            i[1].append(url)
            found = True
            break
    if not found:
        item.append(keyword)
        item.append([url])
        index.append(item)
    return index


def main():
    index = []
    index2 = [['udacity', ['http://udacity.com', 'http://npr.org']],
              ['computing', ['http://acm.org']]]
    
    add_to_index(index,'udacity','http://udacity.com')
    add_to_index(index,'computing','http://acm.org')
    add_to_index(index,'udacity','http://npr.org')
    print(index)
    #>>> [['udacity', ['http://udacity.com', 'http://npr.org']], 
    #>>> ['computing', ['http://acm.org']]]
    print('lookup : {}'.format(lookup(index2,'udacity')))
    #>>> ['http://udacity.com','http://npr.org']


if __name__ == '__main__':
    main()