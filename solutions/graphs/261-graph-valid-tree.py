class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """

        if len(edges) != n-1:
            return False

        root = [i for i in range(n)]
        rank = [1] * n

        for a, b in edges:
            a_root = root[a]
            b_root = root[b]
            if a_root == b_root:
                return False
            if rank[a_root] > rank[b_root]:
                root[b] = a_root
            elif rank[b_root] > rank[a_root]:
                root[a] = b_root
            else:
                root[b] = a_root
                rank[a_root] += 1

        return True


if __name__ == '__main__':
    print(Solution().validTree(n=5, edges=[[0, 1], [0, 2], [0, 3], [1, 4]]))
    print(Solution().validTree(n=5, edges=[[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))
    print(Solution().validTree(n=4, edges=[[0, 1], [2, 3]]))
