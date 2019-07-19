class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        wordDict = set(wordDict)
        dp = [[] for _ in range(len(s))]
        def recursion(start, length):
            print(dp)
            if start == length:
                return []
            if dp[start]:
                return dp[start]
            for i in range(start+1, length+1):
                if s[start:i] in wordDict:
                    print(s[i:])
                    for sub_string in recursion(i, length):
                        dp[start].append(s[start:i] + ' ' + sub_string)
            return dp[start]
        recursion(0, len(s))
        return dp[0]

s = Solution()
print(s.wordBreak("aaaaaaa", ["aaaa","aa","a"]))