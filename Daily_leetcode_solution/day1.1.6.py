class Solution(object):
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """
        num_set = set(nums)  # faster lookup
        
        while original in num_set:
            original *= 2
        
        return original