class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l, r = 0, len(s) - 1
        while l < r:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue

            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1

        return True

    def isPalindromeShort(self, s):
        """
        :type s: str
        :rtype: bool
        """
        input = [i.lower() for i in s if i.isalnum()]

        return input == input[::-1]


if __name__ == '__main__':
    print(Solution().isPalindromeShort(s="A man, a plan, a canal: Panama"))
    print(Solution().isPalindromeShort(s="race a car"))
    print(Solution().isPalindromeShort(s=" "))
