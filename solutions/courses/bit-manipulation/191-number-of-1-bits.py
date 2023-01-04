class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0

        for i in range(32):
            if n & 1:
                count += 1
            n >>= 1
        return count


if __name__ == "__main__":
    print(Solution().hammingWeight(n=int("000000000000000000000000001011", 2)))
    print(Solution().hammingWeight(n=int("000000000000000000000010000000", 2)))
    print(Solution().hammingWeight(n=int("11111111111111111111111111111101", 2)))
