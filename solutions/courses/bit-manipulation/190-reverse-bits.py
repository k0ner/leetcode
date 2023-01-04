class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0
        for i in range(4):
            res <<= 1
            bit = n & 1
            res += bit
            n >>= 1

        return res


if __name__ == "__main__":
    print(f'{Solution().reverseBits(n=int("1100", 2)):b}')
    print(Solution().reverseBits(n=int("1100", 2)))
    print(f'{Solution().reverseBits(n=int("00000010100101000001111010011100", 2)):b}')
    print(Solution().reverseBits(n=int("00000010100101000001111010011100", 2)))
    print(Solution().reverseBits(n=int("11111111111111111111111111111101", 2)))
