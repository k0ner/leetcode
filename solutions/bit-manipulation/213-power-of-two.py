class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        # n & (n-1) == 0
        return n ^ (n - 1) == (2 * n - 1)


if __name__ == "__main__":
    print(Solution().isPowerOfTwo(n=1))
    print(Solution().isPowerOfTwo(n=0))
    print(Solution().isPowerOfTwo(n=-1))
    print(Solution().isPowerOfTwo(n=-16))
    print(Solution().isPowerOfTwo(n=16))
    print(Solution().isPowerOfTwo(n=3))
    print(Solution().isPowerOfTwo(n=pow(2, 20)))
