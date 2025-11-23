class Solution(object):
    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0, float('-inf'), float('-inf')]
        
        for num in nums:
            temp = dp[:]  # copy current state
            for r in range(3):
                new_r = (r + num) % 3
                dp[new_r] = max(dp[new_r], temp[r] + num)
                
        return dp[0]