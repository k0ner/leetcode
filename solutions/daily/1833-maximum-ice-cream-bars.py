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

    def maxIceCreamCount(self, costs, coins):

        sorted_cost = [0] * (min(coins, pow(10, 5))+1)  # can't afford more than coins, we can discard such ice cream

        total_cost = 0
        for cost in costs:
            total_cost += cost
            if cost <= coins:
                sorted_cost[cost] += 1

        if coins >= total_cost:
            return len(costs)

        bars = 0
        i = 0
        while i < len(sorted_cost):
            if i > coins:  # won't be able to afford even if there are no ice cream at this pos
                return bars

            if sorted_cost[i] == 0:
                i += 1
                continue

            # buy as many as possible
            to_buy = min(coins // i, sorted_cost[i])
            sorted_cost[i] -= to_buy
            coins -= to_buy*i
            bars += to_buy
            i+=1

        return bars


if __name__ == '__main__':
    print(Solution().maxIceCreamCount(costs=[1, 3, 2, 4, 1], coins=7))
    print(Solution().maxIceCreamCount(costs=[10, 6, 8, 7, 7, 8], coins=5))
    print(Solution().maxIceCreamCount(costs=[1, 6, 3, 1, 2, 5], coins=20))
