class Solution(object):
    def convertToBase7Num(self, num):
        """
        :type num: int
        :rtype: str
        """
        base = 7
        res = 0
        exp = 0
        original = num
        num = abs(num)
        while num != 0:
            res += (num % base) * pow(10, exp)
            num //= base
            exp += 1

        if original >= 0:
            return str(res)
        else:
            return str(-res)

    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"
        base = 7
        res = ""
        original = num
        num = abs(num)
        while num != 0:
            res = str(num % base) + res
            num //= base

        if original >= 0:
            return res
        else:
            return "-" + res


if __name__ == "__main__":
    print(Solution().convertToBase7(num=100))
    print(Solution().convertToBase7(num=-7))
    print(Solution().convertToBase7(num=-8))
