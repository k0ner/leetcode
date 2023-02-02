from typing import Optional

from utils import *


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre_head = ListNode()
        pre_head.next = head

        prev, next = pre_head, head
        while next and next.next:

            if next.val == next.next.val:
                val = next.val
                while next and next.val == val:
                    next = next.next
                prev.next = next
            else:
                prev, next = next, next.next

        return pre_head.next


if __name__ == '__main__':
    printList(Solution().deleteDuplicates(ListNode.from_list([1, 2, 3, 3, 4, 4, 5])))
    printList(Solution().deleteDuplicates(ListNode.from_list([1, 1, 1, 2, 3])))
    # printList(Solution().deleteDuplicates())
