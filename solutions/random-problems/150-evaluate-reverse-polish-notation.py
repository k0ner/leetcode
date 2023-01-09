from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {'+': lambda l, r: l + r,
               '-': lambda l, r: l - r,
               '*': lambda l, r: l * r,
               '/': lambda l, r: int(l / r)}

        stack = []
        for token in tokens:
            if token in ops:
                right, left = stack.pop(), stack.pop()
                stack.append(ops[token](left, right))
            else:
                stack.append(int(token))

        return stack[0]


if __name__ == '__main__':
    # print(Solution().evalRPN(tokens=["2", "1", "+", "3", "*"]))
    # print(Solution().evalRPN(tokens=["4", "13", "5", "/", "+"]))
    print(Solution().evalRPN(tokens=["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
