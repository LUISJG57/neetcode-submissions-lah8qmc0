class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        maxIsla = 0

        def dfs(r,c):
            if(min(r,c) < 0 or
            r == ROWS or c == COLS
            or grid[r][c] == 0):
                return 0
            grid[r][c] = 0

            area = 1

            area += dfs(r+1,c)
            area += dfs(r-1,c)
            area += dfs(r,c+1)
            area += dfs(r,c-1)
            return area
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    curr = dfs(r,c)
                    maxIsla = max(maxIsla, curr)
        return maxIsla