from utils import *


class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        exists = set()
        to_delete = set()

        pre_head = ListNode()
        pre_head.next = head
        tail = head
        while tail:
            if tail.val in exists:
                to_delete.add(tail.val)
            exists.add(tail.val)
            tail = tail.next

        prev, next = pre_head, head
        while next:
            if next.val in to_delete:
                prev.next = next.next
            else:
                prev = next
            next = prev.next

        return pre_head.next


if __name__ == '__main__':
    printList(Solution().deleteDuplicatesUnsorted(ListNode.from_list([1, 2, 3, 2])))
    printList(Solution().deleteDuplicatesUnsorted(ListNode.from_list([2, 1, 1, 2])))
    printList(Solution().deleteDuplicatesUnsorted(ListNode.from_list([3, 2, 2, 1, 3, 2, 4])))
