from typing import List


class Solution:
    def getDFS(self, image, res, init_color, color, sr, sc, m, n):
        rows = [0, 0, -1, 1]
        columns = [-1, 1, 0, 0]\

        res[sr][sc] = color

        for row, col in zip(rows, columns):
            if 0 <= sr + row < m and 0 <= sc + col < n and image[sr + row][sc + col] == init_color and res[sr + row][sc + col] != color:
                self.getDFS(image, res, init_color, color, sr + row, sc + col, m, n)

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        res = image
        init_color = res[sr][sc]
        m = len(res)
        n = len(res[0])

        self.getDFS(image, res, init_color, color, sr, sc, m, n)

        return res


if __name__ == "__main__":
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr = 1
    sc = 1
    color = 2
    solution = Solution()
    print(solution.floodFill(image, sr, sc, color))
