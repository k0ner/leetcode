from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start = -1
        end = -1
        for interval in intervals:
            if interval[0] <= newInterval[0] <= interval[1]:
                start = interval[0]
            if interval[0] <= newInterval[1] <= interval[1]:
                end = interval[1]

        start = start if start != -1 else newInterval[0]
        end = end if end != -1 else newInterval[1]

        newIntervals = [[start, end]]
        for interval in intervals:
            if interval[1] < start or interval[0] > end:
                newIntervals.append(interval)

        newIntervals.sort()
        return newIntervals

    def insertOpt(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        while i < len(intervals) and intervals[i][0] < newInterval[0]:
            i += 1

        intervals = intervals[:i] + [newInterval] + intervals[i:]

        i, j, n = 0, 1, len(intervals)
        last_i, last_j = i, j
        found = False
        while j < n:
            if intervals[i][1] >= intervals[j][0]:
                found = True
                last_i, last_j = i, j
                intervals[i][0] = min(intervals[i][0], intervals[j][0])
                intervals[i][1] = max(intervals[i][1], intervals[j][1])
                j += 1

            else:
                i += 1
                j += 1

        return intervals[:last_i + 1] + intervals[last_j + (1 if found else 0):]


if __name__ == '__main__':
    print(Solution().insertOpt(intervals=[[1, 3], [6, 9]], newInterval=[2, 5]))
    print(Solution().insertOpt(intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval=[4, 8]))
    print(Solution().insertOpt(intervals=[[1, 5]], newInterval=[2, 3]))
    print(Solution().insertOpt(intervals=[[1, 5]], newInterval=[2, 7]))
    print(Solution().insertOpt(intervals=[[1, 5]], newInterval=[6, 8]))
    print(Solution().insertOpt(intervals=[[1, 2], [3, 4]], newInterval=[6, 8]))
