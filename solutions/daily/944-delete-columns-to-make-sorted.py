class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        delete = 0
        n = len(strs)
        k = len(strs[0])
        for j in range(0, k):
            prev = strs[0][j]
            for i in range(1, n):
                if strs[i][j] < prev:
                    delete += 1
                    break
                prev = strs[i][j]

        return delete


if __name__ == "__main__":
    print(Solution().minDeletionSize(strs=["cba", "daf", "ghi"]))
    # print(Solution().minDeletionSize(strs=["a", "b"]))
    # print(Solution().minDeletionSize(strs=["zyx", "wvu", "tsr"]))
