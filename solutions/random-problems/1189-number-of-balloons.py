import collections
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        cnt = collections.Counter(text)

        single = [cnt[c] for c in "ban"]
        double = [cnt[c]//2 for c in "lo"]

        return min(single+double)
