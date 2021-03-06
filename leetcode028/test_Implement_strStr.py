class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0

        len_needle = len(needle)
        len_haystack = len(haystack)

        if len_needle > len_haystack:
            return -1

        for idx in range(len_haystack - len_needle + 1):
            if haystack[idx:idx+len_needle] == needle:
                return idx
            
        return -1
