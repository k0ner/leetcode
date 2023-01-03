class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        prev = costs[0]
        for i in range(1, len(costs)):
            current = [0]*3
            current[0] = costs[i][0] + min(prev[1], prev[2])
            current[1] = costs[i][1] + min(prev[0], prev[2])
            current[2] = costs[i][2] + min(prev[0], prev[1])
            prev = current
        return min(prev)


if __name__ == "__main__":
    print(Solution().minCost(costs=[[17, 2, 17], [16, 16, 5], [14, 3, 19]]))
    print(Solution().minCost(costs=[[7, 6, 2]]))
