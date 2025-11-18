class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = 0
        n = len(bits)
        
        while i < n - 1:       # Stop before the last bit
            if bits[i] == 1:
                i += 2        # Two-bit character
            else:
                i += 1        # One-bit character
        
        return i == n - 1 