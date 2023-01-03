class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        prev = costs[0]
        k = len(prev)
        for i in range(1, len(costs)):

            current = [0] * k
            for j in range(0, k):
                current[j] = costs[i][j] + min(prev[:j]+ prev[j+1:])
            prev = current
        return min(prev)


if __name__ == "__main__":
    print(Solution().minCostII(costs=[[17, 2, 17], [16, 16, 5], [14, 3, 19]]))
    print(Solution().minCostII(costs=[[1, 5, 3], [2, 9, 4]]))
    print(Solution().minCostII(costs=[[1, 3], [2, 4]]))
    print(Solution().minCostII(costs=[[7, 6, 2]]))
