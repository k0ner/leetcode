class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        n = 2 * numRows - 2
        res = ["" for i in range(n)]

        def hash_int(position):
            mid = n // 2
            if position <= mid:
                return position
            else:
                return n - position

        for i in range(len(s)):
            pos1 = i % n

            res[hash_int(pos1)] += s[i]

        return "".join(res)

if __name__ == '__main__':
    print(Solution().convert(s="PAYPALISHIRING", numRows=3))
    print(Solution().convert(s="PAYPALISHIRING", numRows=4))
    print(Solution().convert(s="A", numRows=1))
