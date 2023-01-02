class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        prev, current = 1, 2

        i = 2
        while i < n:
            temp, current = current, current + prev
            prev = temp

            i += 1

        return current


if __name__ == "__main__":
    print(Solution().climbStairs(n=2))
    print(Solution().climbStairs(n=3))
    print(Solution().climbStairs(n=4))
