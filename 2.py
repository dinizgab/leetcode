from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    curr1, curr2 = l1, l2
    dummy = res = ListNode()

    carry = 0
    while curr1 and curr2:
        sum = curr1.val + curr2.val + carry

        dummy.next = ListNode(sum % 10)
        carry = sum // 10
        dummy = dummy.next
        if curr2.next and not curr1.next:
            curr1.next = ListNode()
        elif curr1.next and not curr2.next:
            curr2.next = ListNode()

        curr1 = curr1.next
        curr2 = curr2.next

    if carry > 0:
        dummy.next = ListNode(val=carry)

    return res.next
