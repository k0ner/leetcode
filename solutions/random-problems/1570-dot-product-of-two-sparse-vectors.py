from typing import List


class SparseVectorHash:
    def __init__(self, nums: List[int]):
        self.nums = {i: nums[i] for i in range(len(nums)) if nums[i]}

    def dotProduct(self, vec: 'SparseVectorHash') -> int:
        return sum([self.nums[i] * vec.nums[i] for i in self.nums if i in vec.nums])


class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = [(i, nums[i]) for i in range(len(nums)) if nums[i]]

    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        i = j = 0
        while i < len(self.nums) and j < len(vec.nums):
            i_ = self.nums[i]
            j_ = vec.nums[j]
            if i_[0] == j_[0]:
                result += i_[1] * j_[1]
                i += 1
                j += 1
            else:
                while i < len(self.nums) and self.nums[i][0] < vec.nums[j][0]:
                    i += 1
                while i < len(self.nums) and j < len(vec.nums) and self.nums[i][0] > vec.nums[j][0]:
                    j += 1

        return result

# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
