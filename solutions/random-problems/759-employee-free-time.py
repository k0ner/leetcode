# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end


class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        schedule = sorted([interval for i in schedule for interval in i], key=lambda k: k.start)

        res = []
        end = schedule[0].start, schedule[0].end
        for s in schedule[1:]:
            if s.start > end:
                res.append(Interval(end, s.start))
            end = max(end, s.end)
        return res


if __name__ == '__main__':
    print(Solution().employeeFreeTime(
        schedule=[[Interval(s[0], s[1]) for s in l] for l in [[[1, 2], [5, 6]], [[1, 3]], [[4, 10]]]]))
    print(Solution().employeeFreeTime(
        schedule=[[Interval(s[0], s[1]) for s in l] for l in [[[1, 3], [6, 7]], [[2, 4]], [[2, 5], [9, 12]]]]))
