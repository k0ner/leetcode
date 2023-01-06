class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        close = {')': '(', '}': '{', ']': '['}

        pars = []

        def pop(arr):
            if not arr:
                return None
            return arr.pop()

        for p in s:
            if p in close:
                if close[p] != pop(pars):
                    return False

            else:
                pars.append(p)

        return not pars


if __name__ == '__main__':
    print(Solution().isValid(s="()"))
    print(Solution().isValid(s="()[]{}"))
    print(Solution().isValid(s="(]"))
    print(Solution().isValid(s="("))
