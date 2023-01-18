class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        temp = x
        new = 0
        while temp > 0:
            new = new * 10 + temp % 10
            temp //= 10

        return new == x


if __name__ == '__main__':
    print(Solution().isPalindrome(x=121))
    print(Solution().isPalindrome(x=-121))
    print(Solution().isPalindrome(x=10))
