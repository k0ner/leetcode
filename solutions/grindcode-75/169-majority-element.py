from typing import List


class Solution:
    def majorityElementDict(self, nums: List[int]) -> int:
        import collections
        return collections.Counter(nums).most_common()[0][0]

    def majorityElement(self, nums: List[int]) -> int:
        majority = 0
        count = 0

        for num in nums:
            if count == 0:
                majority = num
                count = 1
                continue
            if num == majority:
                count += 1
            else:
                count -= 1

        return majority


if __name__ == '__main__':
    print(Solution().majorityElement(nums=[3, 2, 3]))
    print(Solution().majorityElement(nums=[2, 2, 1, 1, 1, 1, 1, 2, 2]))
