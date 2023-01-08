class MyQueue(object):

    def __init__(self):
        self.stack = []
        self.inverted = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if not self.inverted:
            while self.stack:
                self.inverted.append(self.stack.pop())
        return self.inverted.pop()

    def peek(self):
        """
        :rtype: int
        """
        if not self.inverted:
            while self.stack:
                self.inverted.append(self.stack.pop())
        return self.inverted[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.stack and not self.inverted


if __name__ == '__main__':
    myQueue = MyQueue();
    myQueue.push(1)  # queue is: [1]
    myQueue.push(2)  # queue is: [1, 2] (leftmost is front of the queue)
    print(myQueue.peek())  # return 1
    print(myQueue.pop())  # return 1, queue is [2]
    print(myQueue.empty())  # return false
    myQueue.push(3)
    print(myQueue.pop())
    print(myQueue.empty())  # return false
    print(myQueue.pop())
    print(myQueue.empty())  # return false
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
