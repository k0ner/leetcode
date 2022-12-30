class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        while l <= r:
            index = (l + r) // 2
            if nums[index] == target:
                return index
            elif nums[index] > target:
                r = index - 1
            else:
                l = index + 1

        return -1


if __name__ == "__main__":
    print(Solution().search(nums=[5], target=5))
    print(Solution().search(nums=[-1, 0, 3, 5, 9, 12], target=9))
    print(Solution().search(nums=[-1, 0, 3, 5, 9, 12], target=2))
