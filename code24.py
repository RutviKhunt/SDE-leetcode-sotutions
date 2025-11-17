class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        result = []

        def backtrack(start, remain, path):
            if remain == 0:
                result.append(path[:])
                return

            for i in range(start, len(candidates)):
                # Skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # If number is greater than needed, break early
                if candidates[i] > remain:
                    break

                # Choose the current number
                backtrack(i + 1, remain - candidates[i], path + [candidates[i]])

        backtrack(0, target, [])
        return result