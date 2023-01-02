class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split(" ")
        dict = {}
        wordz = set()
        if len(words) != len(pattern):
            return False

        for i in range(len(pattern)):
            if pattern[i] in dict:
                if dict[pattern[i]] != words[i]:
                    return False
            else:
                if words[i] in wordz:
                    return False
                dict[pattern[i]] = words[i]
                wordz.add(words[i])

        return True


if __name__ == "__main__":
    print(Solution().wordPattern(pattern="abba", s="dog dog dog dog"))
    # print(Solution().wordPattern(pattern="abba", s="dog cat cat dog"))
    # print(Solution().wordPattern(pattern="abba", s="dog cat cat fish"))
    # print(Solution().wordPattern(pattern="aaaa", s="dog cat cat dog"))
