class Solution:
    def lengthOfLastWordIter(self, s: str) -> int:
        end = len(s) - 1

        while s[end] == ' ':
            end -= 1

        start = end
        while start >= 0 and s[start] != ' ':
            start -= 1

        return end - start
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.rstrip(" ").split(' ')[-1])

if __name__ == '__main__':
    print(Solution().lengthOfLastWord(s = "Hello World"))
    print(Solution().lengthOfLastWord(s = "   fly me   to   the moon  "))
    print(Solution().lengthOfLastWord(s = "luffy is still joyboy"))
    print(Solution().lengthOfLastWord(s = "luffy"))
