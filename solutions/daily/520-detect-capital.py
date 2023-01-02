class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        # cases:
        # 1. all upper
        # 2. first upper, no more upper-cased
        # 3. all lower-cased

        lower_case_observed = word[0].islower()

        for i in range(1, len(word)):
            letter = word[i]
            if letter.isupper() and not lower_case_observed:
                continue
            if letter.isupper() and lower_case_observed:
                return False
            if i > 1 and not lower_case_observed:
                return False
            lower_case_observed = True

        return True

if __name__ == "__main__":
    print(Solution().detectCapitalUse(word = "USA"))
    print(Solution().detectCapitalUse(word = "FlaG"))
    print(Solution().detectCapitalUse(word = "leetcode"))
    print(Solution().detectCapitalUse(word = "Google"))
    print(Solution().detectCapitalUse(word = "FFFFFFFFFFFFFFFFFFFFf"))
