class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
    

def merge_two_sorted_lists(L1, L2):
    dummy_head = tail = Node()

    while L1 and L2:
        if L1.value < L2.value:
            tail.next, L1 = L1, L1.next
        else:
            tail.next, L2 = L2, L2.next
        tail = tail.next
    
    tail.next = L1 or L2
    return dummy_head.next

L1 = Node(2, Node(5, Node(7, None)))
L2 = Node(3, Node(11, None))
merged_list = merge_two_sorted_lists(L1, L2)

while merged_list:
    print(merged_list.value)
    merged_list = merged_list.next

