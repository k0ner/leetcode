class Tri:
    tri = [0] * 38

    def __init__(self):
        self.tri[0], self.tri[1], self.tri[2] = 0, 1, 1
        for i in range(3, 38):
            self.tri[i] = self.tri[i - 1] + self.tri[i - 2] + self.tri[i - 3]


class Solution(object):
    tri = Tri()

    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.tri.tri[n]


if __name__ == "__main__":
    print(Solution().tribonacci(n=4))
    print(Solution().tribonacci(n=25))
