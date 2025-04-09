'''
https://leetcode.com/problems/design-hashmap/description/

Design HashMap

Design a HashMap without using any built-in hash table libraries.
Implement the MyHashMap class:
MyHashMap() initializes the object with an empty map.

void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.

int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.

void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.
 

Example 1:
Input
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
Output
[null, null, null, 1, -1, null, 1, null, -1]

Explanation
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // The map is now [[1,1]]
myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]
 
Constraints:
0 <= key, value <= 106
At most 104 calls will be made to put, get, and remove.
'''

from __future__ import annotations

class ListNode:
    def __init__(self, key: int = None, value: int = None, next: ListNode = None):
        self.key = key
        self.value = value
        self.next = next

class MyHashMap:

    def __init__(self):
        self.hashmap = [ListNode() for i in range(1000)]

    def hash(self, key: int) -> int:
        return key % len(self.hashmap)

    def put(self, key: int, value: int) -> None:
        cur = self.hashmap[self.hash(key)]
        while cur:
            if cur.key == key:
                cur.value = value
                return
            cur = cur.next
            
        cur.next = ListNode(key, value, None)
            

    def get(self, key: int) -> int:
        cur = self.hashmap[self.hash(key)]
        
        while cur:
            if cur.key == key:
                return cur.value
            cur = cur.next
        
        return -1
        
    def remove(self, key: int) -> None:
        cur = self.hashmap[self.hash(key)]
        
        while cur and cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)