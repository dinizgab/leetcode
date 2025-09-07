from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(
    list1: Optional[ListNode], list2: Optional[ListNode]
) -> Optional[ListNode]:
    dummy = head = ListNode()
    curr1, curr2 = list1, list2

    while curr1 and curr2:
        if curr1.val <= curr2.val:
            dummy.next = curr1
            curr1 = curr1.next
        else:
            dummy.next = curr2
            curr2 = curr2.next

        dummy = dummy.next

    while curr1:
        dummy.next = curr1
        curr1 = curr1.next
        dummy = dummy.next

    while curr2:
        dummy.next = curr2
        curr2 = curr2.next
        dummy = dummy.next

    return head.next
