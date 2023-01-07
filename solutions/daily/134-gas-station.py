class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        import heapq
        n = len(cost)
        for i in range(n):
            gas[i] -= cost[i]

        heap = [(-val, i) for i, val in enumerate(gas)]

        heapq.heapify(heap)

        while heap:
            (val, index) = heapq.heappop(heap)
            current_gas = 0
            i = 0
            while i < n:
                current_gas += gas[(i + index) % n]
                if current_gas < 0:
                    break
                i += 1

            if i == n:
                return index

        return -1


if __name__ == '__main__':
    # print(Solution().canCompleteCircuit(gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2]))
    print(Solution().canCompleteCircuit(gas=[2, 3, 4], cost=[3, 4, 3]))
