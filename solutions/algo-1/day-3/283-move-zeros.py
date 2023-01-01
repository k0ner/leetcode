class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 0
        length = len(nums)

        while i < length:
            # find first 0
            if nums[i] == 0:
                # first first non zero
                if j < i:
                    j = i
                while j < length:
                    if nums[j] != 0:
                        temp = nums[i]
                        nums[i], nums[j] = nums[j], temp
                        break
                    else:
                        j += 1
            if j == length:
                break
            i += 1

        return nums


if __name__ == "__main__":
    print(Solution().moveZeroes(nums=[0, 1, 0, 3, 12]))
    print(Solution().moveZeroes(nums=[0]))
    print(Solution().moveZeroes(nums=[1, 2, 0, 0, 0, 0, 3, 4, 5, 6, 7]))
    print(Solution().moveZeroes(nums=[-1, -100, 3, 99]))
    print(Solution().moveZeroes(nums=[-1]))
    print(Solution().moveZeroes(nums=[1, 2, 3]))
    print(Solution().moveZeroes(nums=[1, 2, 3, 4, 5]))
