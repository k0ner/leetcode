class Solution(object):
    def addBinaryBits(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if a == "0" and b == "0":
            return "0"

        if len(a) >= len(b):
            res = ["0"] * (len(a) + 1)
            a, b = a[::-1], b[::-1]
            carry = 0
            for i in range(len(b)):
                temp_a = int(a[i])
                temp_b = int(b[i])
                res[i] = temp_a ^ temp_b ^ carry
                carry = 1 if temp_a + temp_b + carry > 1 else 0

            i = len(b)
            while i < len(a):
                temp_a = int(a[i])
                res[i] = temp_a ^ carry
                carry &= temp_a
                i += 1

            if carry:
                res[i] = 1
            return "".join(map(str, res[::-1])).lstrip("0")

        else:
            return self.addBinary(b, a)

    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        x, y = int(a, 2), int(b, 2)

        while x:
            x, y = (x & y) << 1, y ^ x

        return bin(y)[2:]


if __name__ == "__main__":
    print(Solution().addBinary(a="11", b="1"))
    print(Solution().addBinary(a="0", b="0"))
    print(Solution().addBinary(a="1010", b="1011"))
    print(Solution().addBinary(a="10", b="1011"))
    print(Solution().addBinary(a="1", b="111"))
