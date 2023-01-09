from typing import List


class Solution:
    def isMajorityElementLin(self, nums: List[int], target: int) -> bool:
        count = 0
        for num in nums:
            if num == target:
                count += 1
            else:
                count -= 1

        return count > 0

    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        if len(nums) == 1:
            return nums[0] == target

        # find smaller index
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                r = mid - 1
            else:
                l = mid + 1

        smaller_index = r

        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                l = mid + 1
            else:
                r = mid - 1

        print(l)
        print(r)


if __name__ == '__main__':
    print(Solution().isMajorityElement(nums=[1, 1, 2, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 7], target=5))
    print(Solution().isMajorityElement(nums=[10, 100, 101, 101], target=101))
