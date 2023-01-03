class Solution(object):
    def robDp(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0]*(len(nums)+1)

        dp[1] = nums[0]
        for i in range(2, len(nums)+1):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])

        return dp[-1]

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev, current = 0, nums[0]

        for i in range(len(nums)-1):
            # temp = current
            prev, current = current, max(current, prev + nums[i+1])

        return current


if __name__ == "__main__":
    print(Solution().rob(nums=[1, 2, 3, 1]))
    print(Solution().rob(nums=[2, 7, 9, 3, 1]))
