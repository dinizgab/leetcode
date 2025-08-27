class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def delete_duplicates(head: ListNode):
    curr = head
    while curr.next is not None:
        if curr.next.value == curr.value:
            curr.next = curr.next.next
        else:
            curr = curr.next
