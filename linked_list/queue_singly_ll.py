class LinkedQueue:
    class _Node:
        __slots__ = '_element', '_next'
        
        def __init__(self, element, next):
            self._element = element
            self._next = next
    
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
    
    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0
    
    def first(self):
        if self.is_empty():
            raise Exception('Empty Queue')
        return self._head._element

    def dequeue(self):
        if self.is_empty():
            raise Exception('Empty Queue')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer
    
    def enqueue(self, e):
        new_node = self._Node(e, None)
        if self.is_empty():
            self._head = new_node
        else:
            self._tail._next = new_node
        self._tail = new_node
        self._size += 1


if __name__ == '__main__':
    queue = LinkedQueue()
    
    for i in range(0, 10, 2):
        queue.enqueue(i)
        print(f'the first element of the queue is: {queue.first()}')
        print(f'the length of the queue is: {len(queue)}')
        print()
    
    for _ in range(0, 10, 2):
        ans = queue.dequeue()
        print(f'popped element is: {ans}')
        print(f'the length of the queue is: {len(queue)}')
        print()