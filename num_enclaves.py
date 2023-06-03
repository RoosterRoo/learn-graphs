# User function Template for python3

from typing import List


class Solution:
    def numberOfEnclaves(self, grid: List[List[int]]) -> int:
        # code here
        n = len(grid)
        m = len(grid[0])
        vis = [[0 for j in range(m)] for i in range(n)]
        queue = []
        for j in range(m):
            if grid[0][j] == 1:
                queue.append((0, j))
                vis[0][j] = 1
            if grid[n - 1][j]:
                queue.append((n - 1, j))
                vis[n - 1][j] = 1

        for i in range(n):
            if grid[i][0] == 1:
                queue.append((i, 0))
                vis[i][0] = 1
            if grid[i][m - 1]:
                queue.append((i, m - 1))
                vis[i][m - 1] = 1

        while queue:
            node = queue.pop(0)
            row = node[0]
            col = node[1]

            nrows = [-1, 0, 1, 0]
            ncols = [0, 1, 0, -1]

            for nrow, ncol in zip(nrows, ncols):
                new_row = row + nrow
                new_col = col + ncol

                if 0 <= new_row < n and 0 <= new_col < m and grid[new_row][new_col] == 1 and vis[new_row][new_col] != 1:
                    vis[new_row][new_col] = 1
                    queue.append((new_row, new_col))

            cnt = 0
            for i in range(n):
                for j in range(m):
                    if grid[i][j] == 1 and vis[i][j] == 0:
                        cnt += 1

        return cnt


# {
# Driver Code Starts
# Initial Template for Python 3


if __name__ == "__main__":
    grid = [[0, 0, 0, 0],
            [1, 0, 1, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0]]

    obj = Solution()
    print(obj.numberOfEnclaves(grid))

# } Driver Code Ends