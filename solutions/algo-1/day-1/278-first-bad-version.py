# The isBadVersion API is already defined for you.

def isBadVersion(version):
    return version >= 1


class Solution(object):

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 0
        r = n
        last_working = 0

        while l <= r:
            version = (l + r) // 2
            is_bad = isBadVersion(version)
            if is_bad:
                r = version - 1
            else:
                l = version + 1
                last_working = version

        return last_working+1

if __name__ == "__main__":
    print(Solution().firstBadVersion(2))
