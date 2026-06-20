class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        directions = [[0,1], [0,-1],[1,0],[-1,0]]
        
        def dfs(r,c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                return 1
            if (r,c) in visited:
                return 0

            visited.add((r,c))
            perim = 0
            for dr, dc in directions:
                perim += dfs(r + dr, c + dc)
            return perim
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    return dfs(r,c)
        return 0