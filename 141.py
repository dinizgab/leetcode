from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycleOnSpace(head: Optional[ListNode]) -> bool:
    seen = set()
    curr = head

    while curr is not None:
        if curr in seen:
            return True

        seen.add(curr)
        curr = curr.next

    return False


def hasCycleO1Space(head: Optional[ListNode]) -> bool:
    fast = slow = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        if fast == slow:
            return True

    return False
