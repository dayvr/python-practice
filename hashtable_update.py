from UnitaryTest.test import evaluate_result

# Updates the value associated with key. If key is already in the
# table, change the value to the new value. Otherwise, add a new entry
# for the key and value.
def hashtable_update(htable,key,value):
    existent = hashtable_lookup(htable, key)
    bucket = hashtable_get_bucket(htable, key)
    updated = False
    print(existent, bucket)
    for i in bucket:
        if i[0] == key:
            i[1] = value
            updated = True
            break
    if not updated:
        hashtable_add(htable, key, value)
    return htable

def hashtable_update_2(htable,key,value):
    existent = hashtable_lookup_list(htable, key)
    if existent:
        existent[1] = value
    else:
        hashtable_add(htable, key, value)
    return htable

# Takes two inputs, a hashtable and a key (string),
# and returns the value associated with that key.
def hashtable_lookup_list(htable,key):
    value = None
    bucket = hashtable_get_bucket(htable, key)
    for i in bucket:
        if i[0] == key:
            value = i
            break
    return value

def hashtable_lookup(htable,key):
    value = None
    bucket = hashtable_get_bucket(htable, key)
    for i in bucket:
        if i[0] == key:
            value = i[1]
            break
    return value

# Adds the key to the hashtable (in the correct bucket), with the correct 
# value and returns the new hashtable.
def hashtable_add(htable,key,value):
    bucket = hashtable_get_bucket(htable, key)
    bucket.append([key, value])
    return htable  
    
    
def hashtable_get_bucket(htable,keyword):
    return htable[hash_string(keyword,len(htable))]

def hash_string(keyword,buckets):
    out = 0
    for s in keyword:
        out = (out + ord(s)) % buckets
    return out

def make_hashtable(nbuckets):
    empty = []
    i = 0
    while i < nbuckets:
        empty.append([])
        i += 1
    return empty

def main():
    # Test adding to hashtable
    table = make_hashtable(5)
    hashtable_add(table,'Bill', 17)
    hashtable_add(table,'Coach', 4)
    hashtable_add(table,'Ellis', 11)
    hashtable_add(table,'Francis', 13)
    hashtable_add(table,'Louis', 29)
    hashtable_add(table,'Nick', 2)
    hashtable_add(table,'Rochelle', 4)
    hashtable_add(table,'Zoe', 14)
    
    exp = [[['Ellis', 11], ['Francis', 13]], [], [['Bill', 17], ['Zoe', 14]], 
    [['Coach', 4]], [['Louis', 29], ['Nick', 2], ['Rochelle', 4]]]
    print('test hashtable_add: {}'.format(evaluate_result(table, expected=exp)))
    
    # Test lookup
    table = [[['Ellis', 11], ['Francis', 13]], [], [['Bill', 17], ['Zoe', 14]],
    [['Coach', 4]], [['Louis', 29], ['Nick', 2], ['Rochelle', 4]]]

    print('test lookup 1: {}'.format(evaluate_result(hashtable_lookup(table, 'Francis'), expected=13)))
    print('test lookup 2: {}'.format(evaluate_result(hashtable_lookup(table, 'Louis'), expected=29)))
    print('test lookup 3: {}'.format(evaluate_result(hashtable_lookup(table, 'Zoe'), expected=14)))

    print(hashtable_lookup(table, 'Zoe'))
    #expected=14

    # Test hashtable_update
    table = [[['Ellis', 11], ['Francis', 13]], [], [['Bill', 17], ['Zoe', 14]],
            [['Coach', 4]], [['Louis', 29], ['Nick', 2], ['Rochelle', 4]]]

    updated_table = [[['Ellis', 11], ['Francis', 13]], [['Zed', 68]], [['Bill', 42], 
                    ['Zoe', 14]], [['Coach', 4]], [['Louis', 29], ['Nick', 2], 
                    ['Rochelle', 94]]]

    hashtable_update_2(table, 'Bill', 42)
    hashtable_update_2(table, 'Rochelle', 94)
    hashtable_update_2(table, 'Zed', 68)
    print('test hashtable_update: {}'.format(evaluate_result(table, expected=updated_table)))

if __name__ == '__main__':
    main()
