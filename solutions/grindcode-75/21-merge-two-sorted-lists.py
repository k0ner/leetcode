def printList(l):
    while l:
        print(l.val, end="->")
        l = l.next
    print()


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def printList(l):
        while l:
            print(l.val, end="->")
            l = l.next
        print()

    @staticmethod
    def from_list(l):
        if not l:
            return None
        head = ListNode(l[0])
        tail = head
        for i in l[1:]:
            tail.next = ListNode(i)
            tail = tail.next

        return head


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        list1, list2 = ListNode.from_list(list1), ListNode.from_list(list2)

        head = ListNode()
        tail = head

        while list1 and list2:

            if list1.val < list2.val:
                elem = list1.val
                list1 = list1.next
            else:
                elem = list2.val
                list2 = list2.next

            tail.next = ListNode(elem)
            tail = tail.next

        the_rest = list1 if list1 else list2

        tail.next = the_rest

        return head.next



if __name__ == '__main__':
    printList(Solution().mergeTwoLists(list1=[1, 2, 4], list2=[1, 3, 4]))
    printList(Solution().mergeTwoLists(list1 = [], list2 = []))
    printList(Solution().mergeTwoLists(list1 = [], list2 = [0]))
