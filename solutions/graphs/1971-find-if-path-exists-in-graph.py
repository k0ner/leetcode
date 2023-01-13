from typing import List


class Solution:
    def validPathDSU(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        root = [i for i in range(n)]
        rank = [1] * n

        def find(i):
            if i == root[i]:
                return root[i]

            root[i] = find(root[i])

            return root[i]

        for edge in edges:
            x, y = edge[0], edge[1]

            x_root = find(x)
            y_root = find(y)

            if x_root != y_root:
                if rank[x_root] > rank[y_root]:
                    root[y_root] = x_root
                elif rank[y_root] > rank[x_root]:
                    root[x_root] = y_root
                else:
                    root[y_root] = x_root
                    rank[x_root] += 1

        return find(source) == find(destination)

    def validPathDfs(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        from collections import defaultdict
        neighbors = defaultdict(set)
        for edge in edges:
            neighbors[edge[0]].add(edge[1])
            neighbors[edge[1]].add(edge[0])

        stack = [source]
        visited = set()

        while stack:
            node = stack.pop()

            if node not in visited:
                visited.add(node)
                if node == destination:
                    return True
                for n in neighbors[node]:
                    if n not in visited:
                        stack.append(n)
        return False

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        from collections import defaultdict
        neighbors = defaultdict(set)
        for edge in edges:
            neighbors[edge[0]].add(edge[1])
            neighbors[edge[1]].add(edge[0])

        queue = [source]
        visited = set()

        while queue:
            node = queue.pop(0)

            if node not in visited:
                visited.add(node)
                if node == destination:
                    return True
                for n in neighbors[node]:
                    if n not in visited:
                        queue.append(n)
        return False


if __name__ == '__main__':
    print(Solution().validPath(n=3, edges=[[0, 1], [1, 2], [2, 0]], source=0, destination=2))
    print(Solution().validPath(n=6, edges=[[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], source=0, destination=5))
    print(Solution().validPath(n=10,
                               edges=[[4, 3], [1, 4], [4, 8], [1, 7], [6, 4], [4, 2], [7, 4], [4, 0], [0, 9], [5, 4]],
                               source=5,
                               destination=9))
