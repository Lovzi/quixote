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

# from collections import Counter
# class Solution(object):
#     def minWindow(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: str
#         """
#         t_d = dict(Counter(t))
#         s_d = t_d.copy()
#         print(s_d)
#         i, j = 0, 0
#         min_str = s
#         while i <= j and j < len(s):
#             if s[j] in s_d:
#                 s_d[s[j]] -= 1
#                 if s_d[s[j]] <= 0:
#                     s_d.pop(s[j])
#             while not s_d and i < j:
#                 min_str = min_str if min_str < s[i:j + 1] else s[i:j + 1]
#                 if s[i] in t_d:
#                     s_d[s[i]] = s_d.get(s[i], 0) + 1
#                 i += 1
#             j += 1
#         return min_str
# s = Solution()
# print(s.minWindow(s = "ADOBECODEBANC", t = "ABC"))


# from collections import Counter
# class Solution(object):
#     def minWindow(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: str
#         """
#         t_d = Counter(t)
#         i, j = 0, 0
#         missing = len(t)
#         min_str = s
#         while j < len(s):
#             missing -= t_d[s[j]] > 0
#             t_d[s[j]] -= 1
#             while t_d[s[i]] < 0 or s[i] in :
#                 min_str = min_str if min_str < s[i:j + 1] else s[i:j + 1]
#                 t_d[s[i]] += 1
#                 i += 1
#             j += 1
#         return min_str
# s = Solution()
# print(s.minWindow(s = "ADOBECODEBANC", t = "ABC"))

# class Solution(object):
#     def exist(self, board, word):
#         """
#         :type board: List[List[str]]
#         :type word: str
#         :rtype: bool
#         """
#         self.board = board
#         self.word = word
#         self.vis = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
#         self.direct = ((1,0), (0, 1), (0, -1), (-1, 0))
#
#     def dfs(self, i, j, index):
#         if index >= len(self.word):
#             return True
#         if self.board[i][j] != self.word[index]:
#             return False
#         result = False
#         for d in self.direct:
#             if not self.vis[i+d[0]][j+d[1]]:
#                 self.vis[i + d[0]][j + d[1]] = True
#                 result = result or self.dfs(i+d[0], j+d[1], index+1)
#         return result
#
#
#

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [1 for i in range(m)]
        for i in range(1, n):
            for j in range(1, m):
                dp[j] = dp[j-1] + dp[j]
        return dp[-1]


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        r, c = len(obstacleGrid), len(obstacleGrid[0])
        dp = []
        flag = 1
        for i in range(c):
            if obstacleGrid[0][i]:
                flag = 0
            dp.append(flag)

        for i in range(1, r):
            dp[0] = int(not obstacleGrid[i][0] and dp[0])
            for j in range(1, c):
                if obstacleGrid[i][j]:
                    dp[j] = 0
                else:
                    dp[j] = dp[j-1] + dp[j]
        return dp[-1]
s = Solution()
print(s.uniquePathsWithObstacles(
[[0,1,0,0,0],[1,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]))