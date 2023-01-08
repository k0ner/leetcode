# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p.val > q.val:
            return self.lowestCommonAncestor(root, q, p)

        if p.val <= root.val <= q.val:
            return root

        if q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)


if __name__ == '__main__':
    print(Solution().lowestCommonAncestor(TreeNode(6, TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5))),
                                                   TreeNode(8, TreeNode(7), TreeNode(9))), p=2, q=8))
    print(Solution().lowestCommonAncestor(TreeNode(6, TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5))),
                                                   TreeNode(8, TreeNode(7), TreeNode(9))), p=2, q=4))
    print(Solution().lowestCommonAncestor(TreeNode(2, TreeNode(1)), p=2, q=1))

