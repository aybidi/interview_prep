class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


def reverse_linked_list(L, start, finish):
    dummy_head = prev = Node(None, L)
    
    # locate start node
    for _ in range(1, start):
        prev = prev.next
    
    curr = prev.next
    # start reverse process
    for _ in range(finish - start):
        nxt = curr.next
        curr.next = nxt.next
        nxt.next = prev.next
        prev.next = nxt
    
    return dummy_head


if __name__ == "__main__":
    L = Node(11, Node(8, Node(3, Node(5, Node(7, Node(2, Node(10, None)))))))
    reversed_ll = reverse_linked_list(L, 2, 4)

    while reversed_ll:
        print(reversed_ll.value)
        reversed_ll = reversed_ll.next