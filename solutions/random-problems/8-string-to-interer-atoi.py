import math


class Solution:

    def wrap(self, res, sign):
        res *= sign
        return int(max(min(math.pow(2, 31) - 1, res), -math.pow(2, 31)))

    def myAtoi(self, s: str) -> int:
        sign = 1
        res = 0
        s = s.lstrip(' ')
        if s:
            if s[0] == '-' or s[0] == '+':
                if s[0] == '-':
                    sign = -1
                s = s[1:]

        for c in s:
            if not c.isdigit():
                return self.wrap(res, sign)
            res = 10 * res + int(c)

        return self.wrap(res, sign)


if __name__ == '__main__':
    print(Solution().myAtoi(s="42"))
    print(Solution().myAtoi(s="     -42"))
    print(Solution().myAtoi(s="4193 with words"))
    print(Solution().myAtoi(s="0032"))
    print(Solution().myAtoi(s="-0032"))
    print(Solution().myAtoi(s="00-32"))
    print(Solution().myAtoi(s="-91283472332"))
    print(Solution().myAtoi(s="  -0012a42"))
