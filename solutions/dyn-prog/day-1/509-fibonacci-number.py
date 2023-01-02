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

if __name__ == "__main__":
    print(Solution().fib(n=0))
    print(Solution().fib(n=1))
    print(Solution().fib(n=2))
    print(Solution().fib(n=3))
    print(Solution().fib(n=4))
    print(Solution().fib(n=5))
    print(Solution().fib(n=6))
    print(Solution().fib(n=100))
