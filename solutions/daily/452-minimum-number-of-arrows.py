class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        count = 0
        index = 0

        points = sorted(points)
        while index < len(points):
            x1, y1 = points[index]
            index += 1
            while index < len(points):
                x2, y2 = points[index]
                if x2 <= y1:
                    index += 1
                    if y1 > y2:
                        y1 = y2
                else:
                    break
            count += 1

        return count

    def findMinArrowShotsOpt(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        count = 1
        points = sorted(points, key=lambda x: x[1])

        y_end = points[0][1]
        for point in points:
            if y_end < point[0]:
                y_end = point[1]
                count += 1

        return count


if __name__ == '__main__':
    print(Solution().findMinArrowShotsOpt(points=[[10, 16], [2, 8], [1, 6], [7, 12]]))
    print(Solution().findMinArrowShotsOpt(points=[[1, 2], [3, 4], [5, 6], [7, 8]]))
    print(Solution().findMinArrowShotsOpt(points=[[1, 2], [2, 3], [3, 4], [4, 5]]))
    print(Solution().findMinArrowShotsOpt(points=[[9, 12], [1, 10], [4, 11], [8, 12], [3, 9], [6, 9], [6, 7]]))
