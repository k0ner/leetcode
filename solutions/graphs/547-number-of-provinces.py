class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)
        root = [i for i in range(n)]
        children = {i: [i] for i in range(n)}

        def union(i, j):
            i_root = root[i]
            j_root = root[j]

            if i_root != j_root:
                children[i_root] += children[j_root]

                for city in children[j_root]:
                    root[city] = i_root
                del children[j_root]

        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j]:
                    union(i, j)

        return len(children)

if __name__ == '__main__':
    # print(Solution().findCircleNum(isConnected=[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
    # print(Solution().findCircleNum(isConnected=[[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
    print(Solution().findCircleNum(isConnected=[[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]))
