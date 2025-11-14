class Solution(object):
    def rangeAddQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[List[int]]
        """
        diff = [[0] * (n + 1) for _ in range(n + 1)]

        # Step 2: apply difference updates
        for r1, c1, r2, c2 in queries:
            diff[r1][c1] += 1
            diff[r1][c2 + 1] -= 1
            diff[r2 + 1][c1] -= 1
            diff[r2 + 1][c2 + 1] += 1

        # Step 3: build final matrix using prefix sums
        mat = [[0] * n for _ in range(n)]

        # prefix sum row-wise
        for i in range(n):
            for j in range(1, n):
                diff[i][j] += diff[i][j - 1]

        # prefix sum column-wise
        for j in range(n):
            for i in range(1, n):
                diff[i][j] += diff[i - 1][j]

        # copy to final result
        for i in range(n):
            for j in range(n):
                mat[i][j] = diff[i][j]

        return mat