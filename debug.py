class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [[False for i in range(n+1)] for j in range(n)]
        # (())()
        max_par = -1
        for i in range(n):
            dp[i][i] = 0
            for j in range(i+1, n+1):
                if (j - i) % 2 == 0:
                    if s[i] == '(' and s[j-1] == ')' and dp[i+1][j-1] is not False:
                        dp[i][j] = dp[i+1][j-1] + 2
                        max_par = max(dp[i][j], max_par)
                    if j >=2 and s[j-2] == '(' and s[j-1] == ')' and dp[i][j-2] is not False:
                        dp[i][j] = dp[i][j - 2] + 2
                        max_par = max(dp[i][j], max_par)
        return max_par
s = Solution()
print s.longestValidParentheses(")()(())())")