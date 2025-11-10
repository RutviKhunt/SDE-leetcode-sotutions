class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        stack = []  # strictly increasing stack of positive values

        for x in nums:
            if x == 0:
                # reset stack on zero
                stack = []
                continue

            # remove larger values
            while stack and stack[-1] > x:
                stack.pop()

            # add new value if not duplicate
            if not stack or stack[-1] < x:
                stack.append(x)
                ans += 1

        return ans