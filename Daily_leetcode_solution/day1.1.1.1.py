class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        operations = 0
        for num in nums:
            if num % 3 != 0:
                operations += 1
        return operations