"""
146. LRU Cache

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

    LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
    int get(int key) Return the value of the key if the key exists, otherwise return -1.
    void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.

 

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4

 
Constraints:

    1 <= capacity <= 3000
    0 <= key <= 104
    0 <= value <= 105
    At most 2 * 105 calls will be made to get and put.

"""


class LRUCache:
    # Your LRUCache object will be instantiated and called as such:
    # obj = LRUCache(capacity)
    # param_1 = obj.get(key)
    # obj.put(key,value)

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            # Call to put to handle LRU placement
            self.put(key, self.cache[key])
        # Return a default of '-1' if key does not exist
        return self.cache.get(key, -1)

    # Method adds key-value to cache and pops the LRU item
    def put(self, key: int, value: int) -> None:
        # Remove key-value if it exists
        self.cache.pop(key, None)
        # Insert key-value at top of key stack
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            # Delete LRU (bottom of key stack)
            del self.cache[next(iter(self.cache))]

"""
A hash-map, i.e. Python Dictionary solution. Time Complexity: O(1) for both get and put.

Beginning with Python 3.7, Dictionary objects naturally store key-value pairs in the order of key insertion. 
So we can very easily identify the least recently used item with a single iteration of the dictionary keys, 
i.e. one can treat dictionary keys like a stack and the first key is the least-recently-used as long as 
we always replace accessed keys back to the top of the stack.

Implementation detail of last line: To iterate the dictionary keys, 
I chose to use a generator object to simply generate a single key: next(iter(self.cache)), 
which is equivalent to list(self.cache.keys())[0] or self.cache.items()[0][0]. 
The reason behind doing this is because we can avoid a little bit of overhead required to generate a whole list of keys, 
which can be more time-consuming when capacity is large; i.e. generate one key O(1) versus a whole list of keys O(k).
"""
