class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)

        # reverse
        l, r = 0, len(nums) - 1
        while l < r:
            temp = nums[l]
            nums[l] = nums[r]
            nums[r] = temp
            l += 1
            r -= 1

        # reverse left
        l, r = 0, k - 1
        while l < r:
            temp = nums[l]
            nums[l] = nums[r]
            nums[r] = temp
            l += 1
            r -= 1

        l, r = k, len(nums) - 1
        while l < r:
            temp = nums[l]
            nums[l] = nums[r]
            nums[r] = temp
            l += 1
            r -= 1

        return nums


if __name__ == "__main__":
    print(Solution().rotate(nums=[1, 2, 3, 4, 5, 6, 7], k=3))
    print(Solution().rotate(nums=[-1, -100, 3, 99], k=2))
    print(Solution().rotate(nums=[-1], k=2))
    print(Solution().rotate(nums=[1, 2, 3], k=2))
    print(Solution().rotate(nums=[1, 2, 3, 4, 5], k=4))
