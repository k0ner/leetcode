from typing import Optional, List

from utils import *


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import heapq
        # heapq.cmp_lt = lambda a, b: a[0] < b[0]
        heap = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))
                lists[i] = lists[i].next

        pre_head = head = ListNode()
        while heap:
            (val, i) = heapq.heappop(heap)
            head.next= ListNode(val)
            head = head.next
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))
                lists[i] = lists[i].next

        return pre_head.next


if __name__ == '__main__':
    printList(Solution().mergeKLists([ListNode.from_list(l) for l in [[1, 4, 5], [1, 3, 4], [2, 6]]]))
    printList(Solution().mergeKLists([ListNode.from_list(l) for l in []]))
    printList(Solution().mergeKLists([ListNode.from_list(l) for l in [[]]]))
