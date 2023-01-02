class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        prev, current = 0, 1
        i = 1
        while i < n:
            temp = current
            current += prev
            prev = temp
            i += 1

        return current

    def fibClosedForm(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        import math
        sqrt5 = math.sqrt(5)
        phi = (1 + sqrt5) / 2
        psi = (1 - sqrt5) / 2
        return int(round((pow(phi, n) + pow(psi, n)) / sqrt5))


if __name__ == "__main__":
    print(Solution().fibClosedForm(n=0))
    print(Solution().fibClosedForm(n=1))
    print(Solution().fibClosedForm(n=2))
    print(Solution().fibClosedForm(n=3))
    print(Solution().fibClosedForm(n=4))
    print(Solution().fibClosedForm(n=5))
    print(Solution().fibClosedForm(n=6))
    print(Solution().fibClosedForm(n=100))
