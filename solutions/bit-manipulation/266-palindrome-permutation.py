class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import string
        mask = [0] * len(string.ascii_lowercase)

        offset = ord('a')
        for c in s:
            mask[ord(c) - offset] ^= 1

        return sum(mask) <= 1


if __name__ == '__main__':
    print(Solution().canPermutePalindrome(s="abdg"))
    print(Solution().canPermutePalindrome(s="a"))
    print(Solution().canPermutePalindrome(s="code"))
    print(Solution().canPermutePalindrome(s="aab"))
    print(Solution().canPermutePalindrome(s="carerac"))
