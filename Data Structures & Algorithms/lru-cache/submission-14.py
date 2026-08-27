class ListNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        # Dummy nodes
        self.head = ListNode()
        self.tail = ListNode()

        self.head.next = self.tail
        self.tail.prev = self.head


    def _remove(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node


    def _add_to_front(self, node):
        first_node = self.head.next

        node.prev = self.head
        node.next = first_node

        self.head.next = node
        first_node.prev = node


    def _make_most_recent(self, node):
        self._remove(node)
        self._add_to_front(node)


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        self._make_most_recent(node)

        return node.val


    def put(self, key: int, value: int) -> None:

        # Existing key
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._make_most_recent(node)
            return

        # New key
        node = ListNode(key, value)
        self.cache[key] = node
        self._add_to_front(node)

        # Too large -> evict LRU
        if len(self.cache) > self.capacity:
            lru = self.tail.prev

            self._remove(lru)
            del self.cache[lru.key]