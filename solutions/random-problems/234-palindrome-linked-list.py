import math
from typing import Optional

from utils import *


class Solution:
    # revert second half
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        length = 0
        temp = head
        while temp:
            temp = temp.next
            length += 1

        start = math.ceil(length / 2)

        prev, temp = None, head
        i = 0
        while i < start:
            prev, temp = temp, temp.next
            i += 1

        while temp:
            temp2 = temp.next
            temp.next = prev
            prev = temp
            temp = temp2

        i = 0
        while i < start:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
            i+=1

        return True

    def isPalindromeSlowFast(self, head: Optional[ListNode]) -> bool:

        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next

            prev = rev
            rev, slow = slow, slow.next
            rev.next = prev

        if fast: # we deal with odd number of elements
            slow = slow.next

        while slow:
            if slow.val != rev.val:
                return False
            slow, rev = slow.next, rev.next

        return True


if __name__ == '__main__':
    # print(Solution().isPalindrome(ListNode.from_list([1, 2, 2, 1])))
    # print(Solution().isPalindrome(ListNode.from_list([1, 2, 3, 2, 1])))
    # print(Solution().isPalindrome(ListNode.from_list([1, 2, 3, 3, 2, 1])))
    # print(Solution().isPalindrome(ListNode.from_list([1, 2])))
    print(Solution().isPalindromeSlowFast(ListNode.from_list([1, 2, 2, 1])))
    print(Solution().isPalindromeSlowFast(ListNode.from_list([1, 2, 3, 2, 1])))
    print(Solution().isPalindromeSlowFast(ListNode.from_list([1, 2, 3, 3, 2, 1])))
    print(Solution().isPalindromeSlowFast(ListNode.from_list([1, 2])))
