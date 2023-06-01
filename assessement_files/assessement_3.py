class Hash:
    def __init__(self, size):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size


    #hash to calculate the given hash
    def _hash(self, key):
        return sum(ord(char) for char in key) % self.size


    #insering k-v pair into hash table
    def insert(self, key, value):
        index = self._hash(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.values[index] = value
                return
            index = (index + 1) % self.size
        self.keys[index] = key
        self.values[index] = value


    #retrieving value of associated key
    def get(self, key):
        index = self._hash(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index = (index + 1) % self.size
        return None


hash_table=Hash(8)

hash_table.insert('sparrow', 'bird')
print(hash_table.get('sparrow'))


"""3.2. We create the Hash object - a table with the size of 8. We insert key ''sparrow' with the value 'bird'
using the insert method. After that the _hash method is called to calculate the value for our key 'sparrow', 
for example the value is 2, the slot at index 2 of the keys array would be empty, so our key is stored ar index 
and its value would be stored at the same index in the values array. When we retrieve the value via get method using
our key => hash_table.get('sparrow'), _hash method is called again and it determines hash value for our key, the key 
'sparrow' is located at slot index 2 and the corresponding value 'bird' will be returned."""


hash_table.insert('crow', 'bird')
print(hash_table.get('crow'))
"""3.3 If we  insert an extra key 'crow' with a value 'bird' using the insert method, the _hash method will be called
again to calculate its value, and let's just assume that value is 2 as well, so hash value is two which means we have 
a case of collision as the slot with index 2 is already occupied, since slot is occupied by key 'sparrow' we won't be 
able to store the key 'crow' at the same index. To handle collision next available slot will be found, moving at 
increments of 1. If index 3 is not occupied, our key will be stored at index 3, with corresponding value bird stored in
the 'values' array. When we use get method to retrieve the value connected with our key after the hash collision, the
same process of calculating the hash value followed by probing is used to find the correct index of where the key
is stored and after that the value is retrieved."""