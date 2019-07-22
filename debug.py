# class Solution(object):
#     def wordBreak(self, s, wordDict):
#         """
#         :type s: str
#         :type wordDict: List[str]
#         :rtype: List[str]
#         """
#         wordDict = set(wordDict)
#         dp = [[] for _ in range(len(s))]
#         def recursion(start, length):
#             print(dp)
#             if start == length:
#                 return []
#             if dp[start]:
#                 return dp[start]
#             for i in range(start+1, length+1):
#                 if s[start:i] in wordDict:
#                     print(s[i:])
#                     for sub_string in recursion(i, length):
#                         dp[start].append(s[start:i] + ' ' + sub_string)
#             return dp[start]
#         recursion(0, len(s))
#         return dp[0]
#
# s = Solution()
# print(s.wordBreak("aaaaaaa", ["aaaa","aa","a"]))

import math
import math


class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        self.array = A
        self.row_len = len(A[0])
        self.A_len = len(A)
        self.cache = {}
        min_ans = math.inf
        for i in range(len(A[0])):
            min_ans = min(min_ans, self.recursion(0, i, i))
        return min_ans

    def recursion(self, height, start, end):
        if height >= self.A_len:
            return 0
        start = start if start > 0 else 0
        end = end if end < self.row_len - 1 else self.row_len - 1
        if (height, start, end) in self.cache:
            return self.cache[(height, start, end)]
        min_tmp = math.inf
        for i in range(start, end + 1):
            min_tmp = min(self.array[height][i] + self.recursion(height + 1, i - 1, i + 1), min_tmp)
        self.cache[(height, start, end)] = min_tmp
        return min_tmp

s = Solution()
print(s.minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]]))


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.string = s
        self.max_val = 0
        self.s_len = len(s)
        self.recursion(0, len(s)-1, {})
        return self.max_val

    def recursion(self, start, end, cache):
        if start > end:
            return True
        if start < 0 or end >= self.s_len:
            return False

        if (start, end) in cache:
            return cache[(start, end)]

        cache[(start, end)] = False
        if self.string[start] == ')':
            self.recursion(start+1, end, cache)
            return False
        if self.string[end] == '(':
            self.recursion(start, end-1, cache)
            return False

        if self.string[start] == '(' and self.string[end] == ')':
            cache[(start, end)] = self.recursion(start+1, end-1, cache)
            if cache[(start, end)]:
                self.max_val = max(self.max_val, end-start+1)
                return True


        for i in range(start, end):
            left = self.recursion(start, i, cache)
            right = self.recursion(i+1, end, cache)
            if  left and right:
                cache[(start, end)] = True
                self.max_val = max(self.max_val, end - start + 1)
                return True
        return False

s = Solution()
print(s.longestValidParentheses(')((()))'))