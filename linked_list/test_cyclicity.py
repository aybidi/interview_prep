class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

def is_cyclic(L):
    slow = fast = L
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow == fast:
            ptr1, ptr2 = L, slow
            while ptr1 !=  ptr2:
                ptr1, ptr2 = ptr1.next, ptr2.next
            return ptr1
    return False
