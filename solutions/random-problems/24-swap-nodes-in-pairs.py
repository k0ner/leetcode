# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from utils import *


class Solution:
    def swapPairsIter(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        prev = None

        while fast and fast.next:
            slow = fast
            if prev:
                prev.next = slow.next
            else:
                head = slow.next
            prev, fast, slow.next.next, slow.next = slow, slow.next.next, slow, slow.next.next

        return head

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        first, second = head, head.next
        first.next = self.swapPairs(second.next)
        second.next = first

        return second


if __name__ == '__main__':
    printList(Solution().swapPairs(ListNode.from_list([1, 2, 3, 4])))
    printList(Solution().swapPairs(ListNode.from_list([])))
    printList(Solution().swapPairs(ListNode.from_list([1])))
