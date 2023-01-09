class Solution:
    def reverseWordsSimple(self, s: str) -> str:
        return " ".join(s.split()[::-1])

    def reverseWords(self, s: str) -> str:
        length = len(s)
        res = ""
        start = -1
        for i in range(length):
            if s[i].isalnum():
                if start == -1:
                    start = i
            if s[i] == " " and start != -1:
                res = s[start:i] + " " + res if len(res) > 0 else s[start:i]
                start = -1
            if i == length -1 and start != -1:
                res = s[start:] + " " + res if len(res) > 0 else s[start:]

        return res


if __name__ == '__main__':
    print(Solution().reverseWords(s="the sky is blue"))
    print(Solution().reverseWords(s="  hello world  "))
    print(Solution().reverseWords(s="a good   example"))
