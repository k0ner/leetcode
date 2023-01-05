class Solution(object):

    cant_jump = set()

    def canJumpGreedy(self, nums):

        def canJumpInner(pos):
            if pos >= len(nums)-1:
                return True
            if pos in self.cant_jump:
                return False
            can_jump = False
            i = pos+nums[pos]
            while i > pos and not can_jump:
                can_jump = canJumpInner(i)
                i -= 1
            if not can_jump:
                self.cant_jump.add(pos)

            return can_jump
        return canJumpInner(0)

    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_index = 0
        for i in range(len(nums)):
            max_index = max(max_index, i + nums[i])
            if max_index >= len(nums) - 1:
                return True
            if max_index == i:
                return False


if __name__ == '__main__':
    print(Solution().canJumpGreedy([1,2]))
    # print(Solution().canJumpGreedy(nums=[2, 3, 1, 1, 4]))
    # print(Solution().canJumpGreedy(nums=[3, 2, 1, 0, 4]))
    # print(Solution().canJumpGreedy(
    #     [2, 0, 6, 9, 8, 4, 5, 0, 8, 9, 1, 2, 9, 6, 8, 8, 0, 6, 3, 1, 2, 2, 1, 2, 6, 5, 3, 1, 2, 2, 6, 4, 2, 4, 3, 0, 0,
    #      0, 3, 8, 2, 4, 0, 1, 2, 0, 1, 4, 6, 5, 8, 0, 7, 9, 3, 4, 6, 6, 5, 8, 9, 3, 4, 3, 7, 0, 4, 9, 0, 9, 8, 4, 3, 0,
    #      7, 7, 1, 9, 1, 9, 4, 9, 0, 1, 9, 5, 7, 7, 1, 5, 8, 2, 8, 2, 6, 8, 2, 2, 7, 5, 1, 7, 9, 6]))
