class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = "1"       # base case
        
        for _ in range(n - 1):
            result = ""
            i = 0
            while i < len(s):
                count = 1
                # count repeated characters
                while i + 1 < len(s) and s[i] == s[i + 1]:
                    count += 1
                    i += 1
                # append count + character
                result += str(count) + s[i]
                i += 1
            s = result
        return s