class Solution(object):
    def earliestAcq(self, logs, n):
        """
        :type logs: List[List[int]]
        :type n: int
        :rtype: int
        """
        root = [i for i in range(n)]
        when_met = -1
        friends = {i: [i] for i in range(n)}

        for timestamp, a, b in sorted(logs):
            a_root = root[a]
            b_root = root[b]

            if a_root != b_root:
                when_met = max(timestamp, when_met)

                friends[a_root] += friends[b_root]
                root[b_root] = a_root
                for friend in friends[b_root]:
                    root[friend] = a_root
                del friends[b_root]

        return -1 if len(friends) != 1 else when_met


if __name__ == '__main__':
    print(Solution().earliestAcq(
        logs=[[20190101, 0, 1], [20190104, 3, 4], [20190107, 2, 3], [20190211, 1, 5], [20190224, 2, 4],
              [20190301, 0, 3], [20190312, 1, 2], [20190322, 4, 5]], n=6))
    print(Solution().earliestAcq(logs=[[0, 2, 0], [1, 0, 1], [3, 0, 3], [4, 1, 2], [7, 3, 1]], n=4))
    print(Solution().earliestAcq(logs=[[7, 3, 1], [2, 3, 0], [3, 2, 1], [6, 0, 1], [0, 2, 0], [4, 3, 2]], n=4))
