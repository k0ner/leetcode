class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"
        base = 16
        hex_map = '0123456789abcdef'
        res = ""

        for i in range(8):
            res = hex_map[num % base] + res
            num //= base

        return res.lstrip('0')


if __name__ == "__main__":
    print(Solution().toHex(num=26))
    print(Solution().toHex(num=-1))
    print(Solution().toHex(num=100))
    print(Solution().toHex(num=-7))
    print(Solution().toHex(num=-8))
