class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        n = len(nums)
        overall_gcd = nums[0]
        for num in nums:
            overall_gcd = gcd(overall_gcd, num)

        # if gcd of entire array > 1 → impossible
        if overall_gcd != 1:
            return -1

        # count existing 1s
        ones = nums.count(1)
        if ones > 0:
            return n - ones  # each non-1 can become 1 using existing 1s

        # if no 1s, find shortest subarray whose gcd = 1
        min_len = float('inf')
        for i in range(n):
            g = nums[i]
            for j in range(i, n):
                g = gcd(g, nums[j])
                if g == 1:
                    min_len = min(min_len, j - i + 1)
                    break

        # total operations = (make one 1) + (spread it)
        return (min_len - 1) + (n - 1)