class Solution(object):
    def findTheDifferenceSort(self, s, t):

        s = sorted(s)
        t = sorted(t)

        for i in range(len(s)):
            if s[i] != t[i]:
                return t[i]
        return t[-1]

    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        total = 0
        for i in range(len(s)):
            total += - ord(s[i]) + ord(t[i])

        total += ord(t[-1])

        return chr(total)

    def findTheDifferenceBit(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        mask = 0
        for i in range(len(s)):
            mask ^= ord(s[i]) ^ ord(t[i])

        mask ^= ord(t[-1])

        return chr(mask)


if __name__ == '__main__':
    print(Solution().findTheDifferenceBit(s="abcd", t="abcde"))
    print(Solution().findTheDifferenceBit(s="", t="y"))
