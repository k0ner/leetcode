class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev, current = 0, nums[0]

        for i in range(len(nums) - 2):
            prev, current = current, max(current, prev + nums[i + 1])

        max_1 = current

        prev, current = 0, nums[-1]
        for i in range(len(nums) - 2, 0, -1):
            prev, current = current, max(current, prev + nums[i])

        return max(max_1, current)

if __name__ == "__main__":
    # print(Solution().rob(nums=[2, 3, 2]))
    # print(Solution().rob(nums=[1, 2, 3, 1]))
    print(Solution().rob(nums=[1, 2, 3]))
