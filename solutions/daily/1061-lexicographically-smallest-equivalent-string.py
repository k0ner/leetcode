class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:

        root = {c: c for c in set(s1 + s2)}
        rank = {c: ord(c) for c in set(s1 + s2)}

        def find(c):
            if c not in root:
                return c
            if root[c] == c:
                return root[c]
            root[c] = find(root[c])
            return root[c]

        def union(c1, c2):
            c1_root = find(c1)
            c2_root = find(c2)
            if c1_root != c2_root:
                if rank[c1_root] < rank[c2_root]:
                    root[c2_root] = c1_root
                else:
                    root[c1_root] = c2_root

        for i in range(len(s1)):
            union(s1[i], s2[i])

        return "".join([find(c) for c in baseStr])


if __name__ == '__main__':
    print(Solution().smallestEquivalentString(s1="parker", s2="morris", baseStr="parser"))
    print(Solution().smallestEquivalentString(s1="hello", s2="world", baseStr="hold"))
    print(Solution().smallestEquivalentString(s1="leetcode", s2="programs", baseStr="sourcecode"))
