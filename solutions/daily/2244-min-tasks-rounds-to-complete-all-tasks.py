import sys


class Solution(object):
    def minimumRoundsDp(self, tasks):
        """
        :type tasks: List[int]
        :rtype: int
        """
        costs = {}
        for task in tasks:
            if task in costs:
                costs[task] += 1
            else:
                costs[task] = 1

        for cost in costs.values():
            if cost < 2:
                return -1

        res = 0
        for cost in costs.values():
            dp = [sys.maxsize] * (cost+1)
            dp[0] = 0
            dp[2] = 1
            for i in range(3, cost+1):
                dp[i] = min(dp[i-2], dp[i-3])+1
            res += dp[-1]

        return res

    def minimumRounds(self, tasks):
        """
        :type tasks: List[int]
        :rtype: int
        """
        costs = {}
        for task in tasks:
            if task in costs:
                costs[task] += 1
            else:
                costs[task] = 1

        for cost in costs.values():
            if cost < 2:
                return -1

        res = 0
        for cost in costs.values():
            prev_0, prev_1 = 0, sys.maxsize
            current = 1
            for i in range(3, cost+1):
                temp = current
                current = min(prev_0, prev_1)+1
                prev_0 = prev_1
                prev_1 = temp
            res += current

        return res


if __name__ == "__main__":
    print(Solution().minimumRounds(tasks=[2, 2, 3, 3, 2, 4, 4, 4, 4, 4]))
    print(Solution().minimumRounds(tasks=[2, 3, 3]))
