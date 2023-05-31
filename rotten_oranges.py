from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        new_grid = grid
        queue = []
        max_time = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if new_grid[i][j] == 2:
                    queue.append(((i, j), 0))

        nrows = [-1, 0, 1, 0]
        ncols = [0, 1, 0, -1]

        while queue:
            node = queue.pop(0)
            row = node[0][0]
            col = node[0][1]
            time = node[1]

            max_time = max(max_time, time)

            for nrow, ncol in zip(nrows, ncols):
                if 0 <= row + nrow < m and 0 <= col + ncol < n and new_grid[row + nrow][col + ncol] != 2 and \
                        new_grid[row + nrow][col + ncol] == 1:
                    new_grid[row + nrow][col + ncol] = 2
                    queue.append(((row + nrow, col + ncol), time + 1))

        if sum([x.count(1) for x in grid]):
            return -1
        return max_time


if __name__ == "__main__":
    grid = [[1, 2]]
    obj = Solution()
    print(obj.orangesRotting(grid))
