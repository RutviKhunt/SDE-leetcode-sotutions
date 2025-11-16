class Solution(object):
    def numSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10**9 + 7
        count = 0
        curr = 0

        for ch in s:
            if ch == '1':
                curr += 1
                count = (count + curr) % MOD
            else:
                curr = 0

        return count