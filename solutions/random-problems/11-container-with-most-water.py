from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        l, r = 0, len(height) - 1

        while l < r:
            max_area = max(max_area, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area


if __name__ == '__main__':
    print(Solution().maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print(Solution().maxArea(height=[1, 1]))
    # print(Solution().maxArea())
