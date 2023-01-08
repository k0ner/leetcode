class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """

        if not len(image) or not len(image[0]):
            return image

        original_color = image[sr][sc]
        visited = set()

        def dfs(i, j):
            if (i, j) not in visited and 0 <= i < len(image) and 0 <= j < len(image[0]):
                visited.add((i, j))
                if image[i][j] == original_color:
                    image[i][j] = color
                    dfs(i - 1, j)
                    dfs(i + 1, j)
                    dfs(i, j - 1)
                    dfs(i, j + 1)

        if image[sr][sc] != color:
            dfs(sr, sc)
        return image


if __name__ == '__main__':
    print(Solution().floodFill(image=[[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr=1, sc=1, color=2))
    print(Solution().floodFill(image=[[0, 0, 0], [0, 0, 0]], sr=0, sc=0, color=0))
