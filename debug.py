class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        dp = [[None for _ in range(len(s)+1)] for _ in range(len(t)+1)]

        def dfs(i, j):
            if dp[i][j] is not None:
                return dp[i][j]
            if i <= 0:
                return 1
            if j <= 0:
                return 0
            dp[i][j] = 0
            if t[i-1] == s[j-1]:
                dp[i][j] = dfs(i - 1, j - 1)
            dp[i][j] += dfs(i, j-1)
            return dp[i][j]
        return dfs(len(t), len(s))
s = Solution()
print(s.numDistinct(s = "babgbag", t = "bag"))





