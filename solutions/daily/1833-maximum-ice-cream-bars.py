class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        costs = sorted(costs)

        bars = 0
        for cost in costs:
            if cost <= coins:
                bars += 1
                coins -= cost

        return bars


if __name__ == '__main__':
    print(Solution().maxIceCream(costs=[1, 3, 2, 4, 1], coins=7))
    print(Solution().maxIceCream(costs=[10, 6, 8, 7, 7, 8], coins=5))
    print(Solution().maxIceCream(costs=[1, 6, 3, 1, 2, 5], coins=20))
