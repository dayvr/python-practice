# Some of the duplicate code in lookup and update could be avoided by a better design.
# bucket_find() will be used in both functions for avoiding code repetition

def bucket_find(bucket, key):
    for entry in bucket:
        if entry[0] == key:
            return entry
    return None

def hashtable_update(htable, key, value):
    bucket = hashtable_get_bucket(htable, key)
    entry = bucket_find(bucket, key)
    if entry:
        entry[1] = value
    else:
        bucket.append([key, value])

def hashtable_lookup(htable, key):
    entry = bucket_find(hashtable_get_bucket(htable, key), key)
    if entry:
        return entry[1]
    return None

def make_hashtable(nbuckets):
    empty = []
    i = 0
    while i < nbuckets:
        empty.append([])
        i += 1
    return empty

def hash_string(s, size):
    h = 0
    for c in s:
         h = h + ord(c)
    return h % size

def hashtable_get_bucket(htable, key):
    return htable[hash_string(key, len(htable))]

def main():    
    table = make_hashtable(10)
    hashtable_update(table, 'Python', 'Monty')
    hashtable_update(table, 'CLU', 'Barbara Liskov')
    hashtable_update(table, 'JavaScript', 'Brendan Eich')
    hashtable_update(table, 'Python', 'Guido van Rossum')
    print(hashtable_lookup(table, 'Python'))
    #>>> Guido van Rossum


if __name__ == '__main__':
    main()
