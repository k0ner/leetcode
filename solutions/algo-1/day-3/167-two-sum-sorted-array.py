class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(numbers)-1

        while l < r:
            val = numbers[l] + numbers[r]
            if val == target:
                return [l+1, r+1]
            elif val > target:
                r -= 1
            else:
                l += 1


if __name__ == "__main__":
    print(Solution().twoSum(numbers=[2, 7, 11, 15], target=9))
    print(Solution().twoSum(numbers=[2, 3, 4], target=6))
    print(Solution().twoSum(numbers=[-1, 0], target=-1))
