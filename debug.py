# class Solution(object):
#     def numDecodings(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         i, ans = 0, 0
#         while i < len(s):
#             if int(s[i:i+2]) > 26:
#                 i += 2
#             else:
#                 i += 1
#             ans += 1
#         return ans
# 
# 
# 
#

from collections import Counter
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        t_d = dict(Counter)
        s_d = t_d[:]
        i, j = 0, 0
        min_str = s
        while i < j:
            if s[j] in s_d:
                s_d -= 1
                if s_d[s[j]] <= 0:
                    s_d.pop(s[j])
            while not s_d and i < j:
                min_str = min_str if min_str < s[i:j + 1] else s[i:j + 1]
                if s[i] in t_d:
                    s_d[s[i]] = s_d.get(s[i], 0) + 1
                i += 1

