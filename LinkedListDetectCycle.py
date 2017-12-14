"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""
def has_cycle(head):
    if head:
        pointer1, pointer2 = head, head
        while pointer1.next and pointer2.next and pointer2.next.next:
                pointer1 = pointer1.next
                pointer2 = pointer2.next.next
                if pointer1 == pointer2:
                    return True
    return False
