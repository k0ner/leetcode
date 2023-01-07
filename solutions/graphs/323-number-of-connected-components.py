class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        root = [i for i in range(n)]

        children = {i: [i] for i in range(n)}
        for x, y in edges:
            x_root = root[x]
            y_root = root[y]

            if x_root != y_root:
                children[x_root] += children[y_root]
                for i in children[y_root]:
                    root[i] = x_root
                del children[y_root]

        return len(children)


if __name__ == '__main__':
    print(Solution().countComponents(n=4, edges=[[0, 1], [2, 3], [1, 2]]))
