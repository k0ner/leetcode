from typing import Optional

from solutions.utils import *


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head.next

        while fast:
            slow = slow.next
            fast = fast.next.next if fast.next else None

        return slow


if __name__ == '__main__':
    printList(Solution().middleNode(ListNode.from_list(l=[1, 2, 3, 4, 5])))
    printList(Solution().middleNode((ListNode.from_list(l=[1, 2, 3, 4, 5, 6]))))
    printList(Solution().middleNode(ListNode.from_list(l=[1])))
