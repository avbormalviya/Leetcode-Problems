
# Problem Statement

"""
Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:

void add(key) Inserts the value key into the HashSet.
bool contains(key) Returns whether the value key exists in the HashSet or not.
void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.
"""


# Solution


class MyHashSet:
    def __init__(self):
        # Initialize the size of the hash set (list of sets)
        self.n = 10000
        # Create a list of empty sets to handle potential hash collisions
        self.hashmap = [set() for _ in range(self.n)]  # Using a set for unique keys

    def add(self, key: int) -> None:
        # Compute the hash index using modulo operation
        # Add the key to the set at the computed index
        self.hashmap[key % self.n].add(key)  # Average time complexity: O(1)

    def remove(self, key: int) -> None:
        # Compute the hash index
        # Remove the key from the set at the computed index if it exists
        self.hashmap[key % self.n].discard(key)  # O(1), avoids KeyError if the key is absent

    def contains(self, key: int) -> bool:
        # Compute the hash index
        # Check if the key exists in the set at the computed index
        return key in self.hashmap[key % self.n]  # Average time complexity: O(1)


if __name__ == "__main__":
    myHashSet = MyHashSet()
    myHashSet.add(1)
    myHashSet.add(2)
    print(myHashSet.contains(1))  # Output: True
    print(myHashSet.contains(3))  # Output: False
    myHashSet.add(2)
    print(myHashSet.contains(2))  # Output: True
    myHashSet.remove(2)
    print(myHashSet.contains(2))  # Output: False
