class Solution(object):
    def missingNumberGauss(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = len(nums) * (len(nums) + 1) // 2
        return s - sum(nums)

    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mask = len(nums)
        for index, num in enumerate(nums):
            mask ^= index ^ num
        return mask


if __name__ == '__main__':
    print(Solution().missingNumber(nums=[3, 0, 1]))
    print(Solution().missingNumber(nums=[0, 1]))
    print(Solution().missingNumber(nums=[9, 6, 4, 2, 3, 5, 7, 0, 1]))
