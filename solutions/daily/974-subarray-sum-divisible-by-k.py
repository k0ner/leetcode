import math
from typing import List
import collections


class Solution:
    def subarraysDivByKBrut(self, nums: List[int], k: int) -> int:
        out = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                if sum(nums[i:j]) % k == 0:
                    out += 1

        return out

    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        cnt = collections.Counter()
        cnt[0] = 1
        running_mod = 0
        for num in nums:
            running_mod = (num + running_mod) % k
            cnt[running_mod] += 1

        return sum([n*(n-1)//2 for n in cnt.values()])


if __name__ == '__main__':
    print(Solution().subarraysDivByK(nums=[4, 5, 0, -2, -3, 1], k=5))
    print(Solution().subarraysDivByK(nums=[5], k=9))
    print(Solution().subarraysDivByK(nums=[5], k=5))
    print(Solution().subarraysDivByK(nums=[-5], k=5))
    print(Solution().subarraysDivByK(nums=[8, 9, 7, 8, 9], k=8))
