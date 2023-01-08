class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        if len(ransomNote) > len(magazine):
            return False

        from collections import Counter

        freq = Counter(magazine)

        for l in ransomNote:
            freq[l] -= 1

        return all([i >= 0 for i in freq.values()])
