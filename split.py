# It update the index to include all of the word occurences found in the
# page content by adding the url to the word's associated url list.

def add_to_index(index,keyword,url):
    for entry in index:
        if entry[0] == keyword:
            entry[1].append(url)
            return
    index.append([keyword,[url]])

def add_page_to_index(index,url,content):
    new_list = content.split(" ")
    for i in new_list:
        add_to_index(index,i,url)

def main():
    index = []
    add_page_to_index(index,'fake.text',"This is a test")
    print(index)
    #>>> [['This', ['fake.text']], ['is', ['fake.text']], ['a', ['fake.text']],
    #>>> ['test',['fake.text']]]
    

if __name__ == '__main__':
    main()
