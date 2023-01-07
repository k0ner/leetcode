# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        if not root:
            return None
        temp = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(temp)

        return root


def printTree(root):
    res = []
    fifo = []
    fifo.append(root)
    while fifo:
        node = fifo.pop(0)
        res.append(node.val)
        if node.left:
            fifo.append(node.left)
        if node.right:
            fifo.append(node.right)

    print(res)

if __name__ == '__main__':
    printTree(TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9))))
    printTree(Solution().invertTree(TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))))
