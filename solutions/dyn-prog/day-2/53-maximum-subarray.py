import sys


class Solution(object):

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_max = maximum = nums[0]

        for i in range(1, len(nums)):
            current_max = max(nums[i], current_max+nums[i])
            maximum = max(maximum, current_max)

        return maximum

    def maxSubArrayBrute(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest = -sys.maxsize
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                largest = max(largest, sum(nums[i:j]))
        return largest


if __name__ == "__main__":
    print(Solution().maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(Solution().maxSubArray(nums=[1]))
    print(Solution().maxSubArray(nums=[5, 4, -1, 7, 8]))
