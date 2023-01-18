from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        start, end = 0, len(nums) - 1

        while start <= end:
            if nums[start] == val:
                # swap

                nums[start], nums[end] = nums[end], nums[start]
                end -= 1
            else:
                start += 1

        return start

    def removeElementNoSwap(self, nums: List[int], val: int) -> int:
        k = 0

        for i in range(len(nums)):
            if nums[i] == val:
                continue
            nums[k] = nums[i]
            k += 1
        return k


if __name__ == '__main__':
    print(Solution().removeElementNoSwap(nums=[], val=1))
    print(Solution().removeElementNoSwap(nums=[1], val=1))
    print(Solution().removeElementNoSwap(nums=[3, 2, 2, 3], val=3))
    print(Solution().removeElementNoSwap(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=2))
    print(Solution().removeElementNoSwap(nums=[0, 4, 4, 0, 4, 4, 4, 0, 2], val=4))
