class HashTable:
    def __init__(self, size):
        self.data = [0] * size

    def _hash(self, key):
        hash = 0 
        for i in range(len(key)):
            hash = (hash + ord(key[i]) * i) % len(self.data)

        return hash

    def set(self, key, value):
        index = self._hash(key)
        if self.data[index] == 0:
            self.data[index] = [[key, value]]
        else:
            self.data[index].append([key, value])
        return
    
    def get(self, key):
        index = self._hash(key)
        if self.data[index] != 0:
            return [value for _, value in self.data[index]]

    def keys(self):
        subset = [self.data[i] for i in range(len(self.data)) if self.data[i] != 0]
        keys_ = []
        for item in subset:
            for entry in item:
                keys_.append(entry[0]) 
        return keys_

table = HashTable(50)
table.set('grapes', 10000)
print(table.get('grapes'))


# Given an array = [2,5,1,2,3,5,1,2,4]
# It should return 2

# Given an array = [2,1,1,2,3,5,1,2,4]
# It should return 1

# Given an array = [2,3,4,5]
# It should returned None

def firstRecurringCharacter(arr):
    nums = {}
    for val in arr:
        if val in nums.keys():
            return val
        else:
            nums[val] = 1