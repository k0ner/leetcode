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
