#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size"""
        self.buckets = [LinkedList() for i in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table"""
        items = ['{}: {}'.format(repr(k), repr(v)) for k, v in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table"""
        return 'HashTable({})'.format(repr(self.items()))

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored"""
        # use the modular of hash with the size of the bucket 
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table"""
        # Collect all keys in each of the buckets
        all_keys = [] # O(1)
        for bucket in self.buckets: #O(b) for b number of iterations
            for key, value in bucket.items(): #O(l), l iterations == n/b
                all_keys.append(key) #O(1)
        return all_keys # n keys


    def values(self):
        """Return a list of all values in this hash table"""
        # Collect all values in each of the buckets
        # O(n). See above.
        all_values = [] # O(1)
        for bucket in self.buckets: #O(b) for b number of iterations
            for key, value in bucket.items(): #O(l), l iterations == n/b
                all_values.append(value) #O(1)
        return all_values # n values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table"""
        # Collect all pairs of key-value entries in each of the buckets
        # O(n). See above again. it's about the same really.
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the length of this hash table by traversing its buckets"""
        # Count number of key-value entries in each of the buckets
        # Worst case: O(n^2) as we have 2 loop
        # Length is O(n), and we're looping through.

        count = 0
        for bucket in self.buckets:
            for key, value in bucket.items():
                count += 1
        return count

    def contains(self, key):
        """Return True if this hash table contains the given key, or False"""
        # Check if the given key exists in a bucket
        # Check bucket O(1), then do a find O(n). 
        # Worst case scenario is O(n) if it's at the end of a bucket.
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        found = bucket.find(lambda item: item[0] == key)

        # return found is not None
        return bool(found)


    def get(self, key):
        """Return the value associated with the given key, or raise KeyError"""
        # TODO: Check if the given key exists and return its associated value
        #  same as above. O(n) again.
        # # average case running time == n/b (average size of linked list)
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        found = bucket.find(lambda item: item[0] == key)

        if found is not None:
            return found[1]
        raise KeyError("Key not longer exists in this hash table")

    def set(self, key, value):
        """Insert or update the given key with its associated value"""
        # TODO: Insert or update the given key-value entry into a bucket
        # 1. find if the given key is found inside the entry
        # 2. bucket has access to the index of the _bucket_index 
        # worst case is Constant. + append which is constant.

        index = self._bucket_index(key)
        bucket = self.buckets[index]

        if self.contains(key):
            self.delete(key)
        self.buckets[index].append((key, value))
     

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError"""
        # Break Down delete in Hash Table. 
        # See "delete" function of linked list;
        # 1. Find the given key and delete its entry if found
        # 2. check if the key is inside the _bucket_index 
        # use found as the lambda function to see if given key matches the key inside the bucket
        # if the item is found, 
        # delete the key inside the key linked list
        # else raise the key error

        # Worst case. O(n) (middle/end)
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        found = bucket.find(lambda item: item[0] == key)
        if found is not None:
            bucket.delete(found)
            return
        else:
            raise KeyError("Key not longer exists in this hash table")

    def get_random_key(self):
        random_num = random.randint(0, int(self.length() - 1))
        return self.keys()[random_num]



def test_hash_table():
    ht = HashTable()
    print(ht)

    print('Setting entries:')
    ht.set('I', 1)
    print(ht)
    ht.set('V', 5)
    print(ht)
    ht.set('X', 10)
    print(ht)
    print('contains(X): ' + str(ht.contains('X')))
    print('get(I): ' + str(ht.get('I')))
    print('get(V): ' + str(ht.get('V')))
    print('get(X): ' + str(ht.get('X')))
    print('length: ' + str(ht.length()))

    # Enable this after implementing delete:
    print('Deleting entries:')
    ht.delete('I')
    print(ht)
    ht.delete('V')
    print(ht)
    ht.delete('X')
    print(ht)
    print('contains(X): ' + str(ht.contains('X')))
    print('length: ' + str(ht.length()))


if __name__ == '__main__':
    test_hash_table()
