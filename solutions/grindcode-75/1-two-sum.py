class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numbers = {}
        for index, num in enumerate(nums):
            if (target - num) in numbers:
                i = numbers[target-num]
                if i != index:
                    return [i, index]

            numbers[num] = index



if __name__ == '__main__':
    print(Solution().twoSum(nums=[2, 7, 11, 15], target=9))
    print(Solution().twoSum(nums=[3, 2, 4], target=6))
    print(Solution().twoSum(nums=[3, 3], target=6))
