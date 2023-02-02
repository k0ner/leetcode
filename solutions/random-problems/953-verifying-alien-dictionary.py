from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alphabet = {c: i for i, c in enumerate(order)}

        for i in range(len(words) - 1):
            first, second = words[i], words[i + 1]

            if len(first) > len(second) and first.startswith(second):
                return False

            j = 0
            while j < min(len(first), len(second))-1 and first[j] == second[j]:
                j += 1
            if alphabet[first[j]] > alphabet[second[j]]:
                return False

        return True


if __name__ == '__main__':
    print(Solution().isAlienSorted(words=["hello", "leetcode"], order="hlabcdefgijkmnopqrstuvwxyz"))
    print(Solution().isAlienSorted(words=["word", "world", "row"], order="worldabcefghijkmnpqstuvxyz"))
    print(Solution().isAlienSorted(words=["apple", "app"], order="abcdefghijklmnopqrstuvwxyz"))
    # print(Solution().isAlienSorted())
