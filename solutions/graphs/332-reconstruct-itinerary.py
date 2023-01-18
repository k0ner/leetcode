import collections
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        flights = collections.defaultdict(list)
        for ticket in tickets:
            from_, to = ticket[0], ticket[1]
            flights[from_].append(to)

        import heapq

        for airport in flights:
            heapq.heapify(flights[airport])

        res = []

        def dfs(start):

            while flights[start]:
                next = heapq.heappop(flights[start])
                dfs(next)

            res.insert(0, start)

        dfs("JFK")
        return res


if __name__ == '__main__':
    print(Solution().findItinerary(tickets=[["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
    print(Solution().findItinerary(
        tickets=[["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]))
