class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        smaller_index = 0
        greater_index = len(nums) - 1
        while l <= r:
            index = (l + r) // 2
            if nums[index] == target:
                return index
            elif nums[index] > target:
                greater_index = index
                r = index - 1
            else:
                smaller_index = index
                l = index + 1

        if nums[smaller_index] > target:
            return smaller_index
        return smaller_index + 1


if __name__ == "__main__":
    print(Solution().searchInsert(nums=[1, 3, 5, 6], target=5))
    print(Solution().searchInsert(nums=[1, 3, 5, 6], target=2))
    print(Solution().searchInsert(nums=[1, 3, 5, 6], target=7))
