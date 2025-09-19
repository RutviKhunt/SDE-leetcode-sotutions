class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        # Start with the first word as prefix
        prefix = strs[0]

        # Compare prefix with each word
        for word in strs[1:]:
            # Shorten prefix until it matches the beginning of word
            while not word.startswith(prefix):
                prefix = prefix[:-1]  # remove last character
                if not prefix:
                    return ""  # no common prefix

        return prefix