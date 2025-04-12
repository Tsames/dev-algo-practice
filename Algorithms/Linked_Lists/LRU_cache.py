"""
https://neetcode.io/problems/lru-cache

LRU Cache
Implement the Least Recently Used (LRU) cache class LRUCache. The class should support the following operations

LRUCache(int capacity) Initialize the LRU cache of size capacity.

int get(int key) Return the value corresponding to the key if the key exists, otherwise return -1.

void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the introduction of the new pair causes the cache to exceed its capacity, remove the least recently used key.

A key is considered used if a get or a put operation is called on it.

Ensure that get and put each run in O(1) average time complexity.

Example 1:
Input:
["LRUCache", [2], "put", [1, 10],  "get", [1], "put", [2, 20], "put", [3, 30], "get", [2], "get", [1]]
Output:
[null, null, 10, null, null, 20, -1]

Explanation:
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 10);  // cache: {1=10}
lRUCache.get(1);      // return 10
lRUCache.put(2, 20);  // cache: {1=10, 2=20}
lRUCache.put(3, 30);  // cache: {2=20, 3=30}, key=1 was evicted
lRUCache.get(2);      // returns 20 
lRUCache.get(1);      // return -1 (not found)
Constraints:

1 <= capacity <= 100
0 <= key <= 1000
0 <= value <= 1000
"""

from __future__ import annotations


class DoubleLinkedListNode:
    def __init__(
        self,
        value: int = None,
        prev: DoubleLinkedListNode = None,
        next: DoubleLinkedListNode = None,
    ):
        self.value = value
        self.prev = prev
        self.next = next


class LRUCache:
    """
    We know that both our get and our put methods needs to have an O(1) average time complexity.
    The difficult part about this problem is removing the least recently used key when the cache goes over capacity in O(1) time.
    We can't simply keep track of the order that values are accessed using a queue because a value could be revisited, and then the data at the front of the queue would indicate a value that was not the least recently used value.

    So lets start with what we do know.
    We know, that we are going to have to store key - value pairs in a dictionary to have a get method with O(1) time.
    Lets name this dictionary map and initilaize it in the constructor

    We know that everytime we get a key-value pair from the cache that we will look up the key given in map.
    If it exists, then return its value.
    If it doesn't exist, then return -1
    No we know that we will have to do some operation in get to indicate that this value has been most recently used.
    We don't know what that is for the moment, so we leave it blank for now.

    Lets now think about how we can keep track of which values have been recently used.
    Would an array work? Each time we access or add a key, we could add it to our array.
    This is just strictly worse than a queue, because we would be looking at the zeroth index, which could be mistaken due to repeat access.
    Additionally, removing the element at the front of an array would immediately cost us O(capacity)

    We know queues don't help. They improve the run time from O(capacity) to O(1), but they could still be potentially incorrect due to repeat access.

    Stacks don't help us much either because they only provide quick access to the element on top, which would be the most recently used element rather than the least recently used element.

    What about linked lists?
    Linked lists have some potential because you can add and remove nodes in O(1) time complexity so long as you have a reference to that node. The difficult comes from the fact that typically to access the nodes you have to travel through the list to find it, which has a worst case of O(n) time complexity.

    So lets think about this.
    Each time we access or add a key, we could create a Node with that key as its value.
    Then we would attach it to the last node in the sequence, so that the last recently used node is at the front of the list.

    But this doesn't fix our problem of repeat access. We have to remove the key from its previous ordering and add it to the back of our linked list everytime we access it again.

    Instead of traversing the linked list to find a node with the same key, we could store reference to it in a dictionary, using the key as the key.

    Then we would have O(1) speed to find our node in question. But we couldn't completely fix the ordering because the node in front of it would still point to it.

    If our list was a doubly Linked list, we could get access to the node in front and behind it.

    We'd also need a variable to store a pointer to the last node in the list.
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.values = {}
        self.nodes = {}
        self.head = DoubleLinkedListNode()
        self.tail = self.head

    def get(self, key: int) -> int:
        """
        Get the value corresponding to the key if it exists
        Otherwise, return -1

        Then, make sure the key is moved to the most recently used. Aka, the end of the our linked list
        """
        if key in self.values:
            # Reorder this key value pair in our list
            self.reorderNodeAtEndOfList(key)
            return self.values[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        """
        1. If the key already exists, update the value
        2. If the key does not exist, then add it along with its corresponding value
        3. Lastly, remove the least recently used key if the cache is overcapacity with the addition of the new key-value pair
        """
        # Key is in map. Alter its value and change its ordering in our linked list
        if key in self.values:
            self.values[key] = value

            # If our key is in our map, then it has a corresponding node in nodes already.
            # We just have to reorder it
            self.removeNodeFromList(key)
            self.reorderNodeAtEndOfList(key)
        # Key is not in our map.
        else:
            # The size of our map is not over capacity.
            # So just add the key to our map, make a node for it, and add it to the end of our list
            if len(self.values) < self.capacity:
                self.values[key] = value
                newNode = DoubleLinkedListNode(key)
                self.nodes[key] = newNode
                self.reorderNodeAtEndOfList(key)
            # The size of our map is over capacity
            else:
                # First of all, lets get rid of the least recently used key-value pair
                lru = self.head.next

                # Remove the LRU from our list
                self.removeNodeFromList(lru.value)

                # Remove the LRU from our dictionaries
                del self.nodes[lru.value]
                del self.values[lru.value]

                # Now add our new key-value pair to the map
                self.values[key] = value

                # Create our new node and add it to the back of the list
                newNode = DoubleLinkedListNode(key)
                self.nodes[key] = newNode
                self.reorderNodeAtEndOfList(key)
                
    def reorderNodeAtEndOfList(self, key: int) -> None:
        targetNode = self.nodes[key]
        
        self.tail.next = targetNode
        targetNode.prev = self.tail
        self.tail = targetNode
        
    def removeNodeFromList(self, key) -> None:
        targetNode = self.nodes[key]
        
        targetNode.prev.next = targetNode.next
        targetNode.next.prev = targetNode.prev

lRUCache = LRUCache(2)
lRUCache.put(1, 10);  # cache: {1=10}
lRUCache.get(1);      # return 10
lRUCache.put(2, 20);  # cache: {1=10, 2=20}
lRUCache.put(3, 30);  # cache: {2=20, 3=30}, key=1 was evicted
lRUCache.get(2);      # returns 20 
lRUCache.get(1);      # return -1 (not found)