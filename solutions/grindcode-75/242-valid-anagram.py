class Solution(object):
    def isAnagramSimple(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)

    def isAnagramFreq(self, s, t):
        if len(s) != len(t):
            return False

        import string
        freq = {i : 0 for i in string.ascii_lowercase}
        for i in range(len(s)):
            freq[s[i]] += 1
            freq[t[i]] -= 1

        return not any(freq.values())

    def isAnagram(self, s, t):
        return self.isAnagramFreq(s,t)


if __name__ == '__main__':
    print(Solution().isAnagram(s="anagram", t="nagaram"))
    print(Solution().isAnagram(s="rat", t="car"))
