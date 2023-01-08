class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        def height(node):
            if not node:
                return 0
            return 1 + max(height(node.left), height(node.right))

        return abs(height(root.left) - height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
    def isBalancedOpt(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        def heightWithBalanced(node):
            if not node:
                return 0, True

            left_height, left_balanced = heightWithBalanced(node.left)
            if not left_balanced:
                return -1, False
            right_height, right_balanced = heightWithBalanced(node.right)
            if not right_balanced:
                return -1, False
            return 1 + max(left_height, right_height), abs(left_height - right_height) <= 1

        return heightWithBalanced(root)[1]


if __name__ == '__main__':
    print(Solution().isBalancedOpt(TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))),
                                         TreeNode(1, TreeNode(0), TreeNode(8)))))
    print(Solution().isBalancedOpt(TreeNode(1, TreeNode(2, TreeNode(3)))))
    print(Solution().isBalancedOpt(TreeNode(1, TreeNode(2, TreeNode(3)), TreeNode(2, None, TreeNode(3, TreeNode(4, None, TreeNode(4)))))))

