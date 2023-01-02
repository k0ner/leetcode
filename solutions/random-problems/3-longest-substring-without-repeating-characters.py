class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0

        l, r = 0, 1
        index = {s[l]: l}

        longest = 1
        while r < len(s):
            if s[r] in index:
                l = max(index[s[r]], l)
            index[s[r]] = r
            current_length = r - l

            r = max(r, l) + 1

            longest = max(longest, current_length)

        return longest

    def lengthOfLongestSubstringSet(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0

        l, r = 0, 1
        exists = set()

        # handel s[0]
        exists.add(s[l])
        longest = 1
        while r < len(s):
            if s[r] in exists:
                exists.remove(s[l])
                l += 1
                continue
            if s[r] not in exists:
                exists.add(s[r])
                current_length = len(exists)
                if current_length > longest:
                    longest = current_length
                r += 1

        return longest


if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring(s="abcabcbb"))
    print(Solution().lengthOfLongestSubstring(s="a"))
    print(Solution().lengthOfLongestSubstring(s="bbbbb"))
    print(Solution().lengthOfLongestSubstring(s="pwwkew"))
    print(Solution().lengthOfLongestSubstring(s="tmmzuxt"))
