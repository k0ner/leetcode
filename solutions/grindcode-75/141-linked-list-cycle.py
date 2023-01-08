from solutions.utils import *


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False

        slow = head
        fast = head.next

        while slow != fast:

            if not fast or not fast.next:
                return False

            fast = fast.next.next
            slow = slow.next

        return True

if __name__ == '__main__':
    # l1 = ListNode.from_list([3, 2, 0, -4])
    # l1.tail.next = l1.next
    # print(Solution().hasCycle(l1))
    #
    # l2 = ListNode.from_list([1, 2])
    # l2.tail.next = l2
    # print(Solution().hasCycle(l2))

    print(Solution().hasCycle(ListNode(1)))
