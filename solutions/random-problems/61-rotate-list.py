class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if not head or not k:
            return head

        length = 1
        tail = head
        while tail.next:
            length += 1
            tail = tail.next

        k = (length - (k % length))% length

        if not k:
            return head

        old_head = head
        while k-1:
            head = head.next

            k -= 1

        prev = head
        head = head.next
        prev.next = None
        tail.next = old_head

        return head


def printList(l):
    while l:
        print(l.val, end = "->")
        l = l.next
    print()

if __name__ == '__main__':
    printList(Solution().rotateRight(head=ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), k=2))
    printList(Solution().rotateRight(head=ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), k=5))
    # printList(Solution().rotateRight(head=ListNode(0, ListNode(1, ListNode(2))), k=4))
    # printList(Solution().rotateRight(head=None, k=4))
