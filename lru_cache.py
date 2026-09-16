class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    """LRU cache: hash map (key -> node) + doubly linked list ordered by
    recency, so both get and put are O(1). List holds a dummy head/tail;
    most-recently-used sits right after head, least-recently-used right
    before tail.

    Use when: "design a cache with O(1) get/put that evicts least
    recently used", or any "design X" question needing fast lookup +
    fast reordering/eviction.

    Cache strategy variants (same map+list skeleton, different eviction
    rule):
    - LFU (least frequently used): evict lowest access count instead of
      oldest; needs a frequency counter alongside the list.
    - FIFO: evict in insertion order; skip the "move to front on get"
      step entirely (implement with a plain deque).
    - TTL: attach an expiry to each node, evict/ignore on access if
      expired.

    Time: O(1) per op. Space: O(capacity).
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.map = {}
        self.head = Node()  # most-recently-used side
        self.tail = Node()  # least-recently-used side
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _insert_at_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key not in self.map:
            return -1
        node = self.map[key]
        self._remove(node)
        self._insert_at_front(node)
        return node.val

    def put(self, key, val):
        if key in self.map:
            self._remove(self.map[key])
        node = Node(key, val)
        self.map[key] = node
        self._insert_at_front(node)
        if len(self.map) > self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.map[lru.key]


if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, "a")
    cache.put(2, "b")
    assert cache.get(1) == "a"  # 1 now most recent
    cache.put(3, "c")  # evicts 2 (least recently used)
    assert cache.get(2) == -1
    assert cache.get(3) == "c"
    assert cache.get(1) == "a"
    print("ok")
