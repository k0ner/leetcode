class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen_once = 0
        seen_twice = 0
        for num in nums:
            seen_once = ~seen_twice & (seen_once^num)
            seen_twice = ~seen_once & (seen_twice^num)

        return seen_once


if __name__ == "__main__":
    print(Solution().singleNumber(nums=[2, 2, 3, 2]))
    print(Solution().singleNumber(nums=[0, 1, 0, 1, 0, 1, 99]))
    print(Solution().singleNumber(nums=[1, 2, 3, 1, 2, 1, 2]))
