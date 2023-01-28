class Solution:
    def maxValue(self, n: str, x: int) -> str:
        x = str(x)
        op = lambda y: y >= x
        i = 0
        if n[0] == '-':
            op = lambda y: y <= x
            i += 1

        while i < len(n) and op(n[i]):
            i += 1

        return n[:max(i, 0)] + x + n[i:]


if __name__ == '__main__':
    print(Solution().maxValue(n="99", x=9))
    print(Solution().maxValue(n="-13", x=2))
    print(Solution().maxValue(n="-132", x=3))
    # print(Solution().maxValue())
