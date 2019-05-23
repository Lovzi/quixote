class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        i, ans = 0, 0
        while i < len(s):
            if int(s[i:i+2]) > 26:
                i += 2
            else:
                i += 1
            ans += 1
        return ans




