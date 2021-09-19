class CircularArrayQueue:
    def __init__(self, capacity):
        self._write = 0
        self._read = 0
        self._A = [None] * capacity

    def __len__(self):
        return self._write - self._read

    def __str__(self):
        return f"list is: {self._A}"
    
    def enqueue(self, element):
        index_to_write_at = self._write % len(self._A)
        if (index_to_write_at + 1) % len(self._A) == self._read:
            raise Exception('Queue is full')
        self._A[index_to_write_at] = element
        self._write = (self._write + 1) % len(self._A)
    
    def dequeue(self):
        if self._read == self._write:
            raise Exception('Queue is empty')
        answer = self._A[self._read]
        self._A[self._read] = None
        self._read = (self._read + 1) % len(self._A)
        return answer


if __name__ == '__main__':
    circularQueue = CircularArrayQueue(5)
    for i in range(4):
        circularQueue.enqueue(i)
        print(len(circularQueue))
        print(circularQueue)

    print("=============")

    for _ in range(5):
        circularQueue.dequeue()
        print(len(circularQueue))
        print(circularQueue)
