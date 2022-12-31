class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 1. find first non-negative (pivot element <- left from it array will be sorted in reserve order,
        # -> right from it in natural order : complexity O(n)
        # 2. square all the elements
        # 3. initiate new array
        # 4. merge 2 arrays, the one left from pivot in reverse order, the one on the right in natural order

        # find first non-negative
        # if first_non_negative is None then array is sorted in reverse order and it could be an optimization but
        # it is not a generalized solution
        first_non_negative = None
        for i in range(len(nums)):
            if nums[i] >= 0:
                first_non_negative = i
                break

        # square all the elements
        for i in range(len(nums)):
            nums[i] *= nums[i]

        dup = [0] * len(nums)

        if first_non_negative is None:
            l = len(nums) - 1
            r = len(nums)
        else:
            l = first_non_negative - 1
            r = first_non_negative
        index = 0
        while l >= 0 and r < len(nums):
            if nums[l] < nums[r]:
                dup[index] = nums[l]
                l -= 1
            else:
                dup[index] = nums[r]
                r += 1
            index += 1

        while l >= 0:
            dup[index] = nums[l]
            l -= 1
            index += 1

        while r < len(nums):
            dup[index] = nums[r]
            r += 1
            index += 1

        return dup


if __name__ == "__main__":
    print(Solution().sortedSquares(nums=[-4, -1, 0, 3, 10]))
    print(Solution().sortedSquares(nums=[0, 3, 10]))
    print(Solution().sortedSquares(nums=[-7, -3, 2, 3, 11]))
    print(Solution().sortedSquares(nums=[-1]))
    print(Solution().sortedSquares(nums=[-11, -9, -5, -3, -2, -1]))
