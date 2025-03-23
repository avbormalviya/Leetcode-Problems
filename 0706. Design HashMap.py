
# Problem Statement

"""
Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

MyHashMap() initializes the object with an empty map.
void put(int key, int value) inserts a (key, value) pair into the HashMap.
If the key already exists in the map, update the corresponding value.
int get(int key) returns the value to which the specified key is mapped,
or -1 if this map contains no mapping for the key.
void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.
"""


# Solution


class MyHashMap:
    def __init__(self):
        self.n = 10000
        self.hashmap = [[] for _ in range(self.n)]

    def put(self, key: int, value: int) -> None:
        index = key % self.n
        for i, (k, v) in enumerate(self.hashmap[index]):
            if k == key:
                self.hashmap[index][i] = (key, value)  # Update value
                return
        self.hashmap[index].append((key, value))  # Insert new key-value pair

    def get(self, key: int) -> int:
        index = key % self.n
        for k, v in self.hashmap[index]:
            if k == key:
                return v  # Return value if key is found
        return -1  # Key not found

    def remove(self, key: int) -> None:
        index = key % self.n
        self.hashmap[index] = [(k, v) for k, v in self.hashmap[index] if k != key]  # Remove key-value pair


if __name__ == "__main__":
    my_hashmap = MyHashMap()
    my_hashmap.put(1, 1)
    my_hashmap.put(2, 2)
    assert my_hashmap.get(1) == 1
    assert my_hashmap.get(3) == -1
    my_hashmap.put(2, 1)
    assert my_hashmap.get(2) == 1
    my_hashmap.remove(2)
    assert my_hashmap.get(2) == -1

    print("All tests passed!")
