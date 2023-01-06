class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        mins = [i for i in prices]
        maxs = [i for i in prices]

        current_min = pow(10, 4) + 1
        for i in range(len(prices)):
            current_min = min(current_min, prices[i])
            mins[i] = current_min

        current_max = 0
        for i in range(len(prices) - 1, -1, -1):
            current_max = max(current_max, prices[i])
            maxs[i] = current_max

        return max([maxs[i] - mins[i] for i in range(len(prices))])

    def maxProfitOpt(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        current_min = prices[0]

        max_profit = 0

        for price in prices:
            current_min = min(price, current_min)
            max_profit = max(max_profit, price - current_min)
        return max_profit


if __name__ == '__main__':
    print(Solution().maxProfit(prices=[7, 1, 5, 3, 6, 4]))
    print(Solution().maxProfit(prices=[7, 6, 4, 3, 1]))
