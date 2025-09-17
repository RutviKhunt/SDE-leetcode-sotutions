class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0

        # Step 1: Find initial rotten oranges & count fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))  # (row, col, minute)
                elif grid[r][c] == 1:
                    fresh += 1

        minutes = 0

        # Step 2: BFS to spread rotting
        while queue:
            r, c, minutes = queue.popleft()
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:  # 4 directions
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2   # rot the fresh orange
                    fresh -= 1
                    queue.append((nr, nc, minutes + 1))

        # Step 3: Check if all fresh oranges are rotten
        return minutes if fresh == 0 else -1