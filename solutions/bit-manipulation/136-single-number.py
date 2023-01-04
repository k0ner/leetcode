class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for num in nums:
            res ^= num

        return res

if __name__ == "__main__":
    print(Solution().singleNumber(nums = [2,2,1]))
    print(Solution().singleNumber(nums = [4,1,2,1,2]))
    print(Solution().singleNumber(nums = [1]))
