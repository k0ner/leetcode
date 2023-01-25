import collections
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_degrees = [0] * numCourses
        follow_ups = collections.defaultdict(set)
        visited = set()

        for prerequisite in prerequisites:
            in_degrees[prerequisite[0]] += 1
            follow_ups[prerequisite[1]].add(prerequisite[0])

        queue = [i for i in range(numCourses) if not in_degrees[i]]
        res = []
        while queue:
            q = queue.pop(0)
            visited.add(q)
            res.append(q)
            for i in follow_ups[q]:
                in_degrees[i] -= 1
                if not in_degrees[i] and i not in visited:
                    queue.append(i)

        return res if len(visited) == numCourses else []


if __name__ == '__main__':
    # print(Solution().findOrder(numCourses=2, prerequisites=[[1, 0]]))
    # print(Solution().findOrder(numCourses=4, prerequisites=[[1, 0], [2, 0], [3, 1], [3, 2]]))
    # print(Solution().findOrder(numCourses=1, prerequisites=[]))
    print(Solution().findOrder(numCourses=3, prerequisites=[[1, 0], [1, 2], [0, 1]]))
    # print(Solution().findOrder())
