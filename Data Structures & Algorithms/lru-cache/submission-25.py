class LRUCache:
    class ListNode:
        def __init__(self, val):
            self.next = None
            self.prev = None
            self.val = val
        
        def __str__(self):
            return f"{self.val}"
        def __repr__(self) -> str:
            return f"{self.val}"

    def __init__(self, capacity: int):
        self._linked_list_root = None
        self._linked_list_tail = self._linked_list_root
        self._h = {}
        self._capacity = capacity

    def get(self, key: int) -> int:
        item = self._h.get(key)
        if item is None:
            return -1
        
        val, llNode = item
        # no need to update if it's already in the tail(least recently accessed)
        if self._linked_list_tail.val != key:
            prev = llNode.prev
            if next_ := llNode.next:
                next_.prev = prev

                if prev:
                    prev.next = next_
                
            prevTail = self._linked_list_tail
            self._linked_list_tail = llNode
            prevTail.next = llNode
            llNode.prev = prevTail

            if llNode is self._linked_list_root:
                self._linked_list_root = self._linked_list_root.next

            llNode.next = None

        return val
        

    def put(self, key: int, value: int) -> None:
        if key in self._h:
            self.get(key)
            self._h[key] = (value, self._h[key][1])
            return

        node = self.ListNode(key)
        node.prev = self._linked_list_tail
        # if root
        if self._linked_list_tail is None:
            self._linked_list_tail = node
            self._linked_list_root = node
        else:
            self._linked_list_tail.next = node
            self._linked_list_tail = node

        self._h[key] = (value, node)
        if len(self._h) > self._capacity and self._linked_list_root:
            root = self._linked_list_root
            if root.next:
                root.next.prev = None

            self._linked_list_root = root.next
            del self._h[root.val]
    
            
        

