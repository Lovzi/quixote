class Solution:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0

        nums, area = [int(''.join(row), base=2) for row in matrix], 0

        for i in range(len(nums)):
            num = -1
            for j in range(i, len(nums)):
                num &= nums[j]

                if not num:
                    break

                n, l = num, 0
                while n:
                    l += 1
                    n &= n << 1

                area = max(area, l * (j - i + 1))

        return area

s = Solution()
print(s.maximalRectangle([
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]))



# class Solution(object):
#     def wordBreak(self, s, wordDict):
#         """
#         :type s: str
#         :type wordDict: List[str]
#         :rtype: List[str]
#         """
#
#         def sentence(s, wordDict, wordLen, i, memo):
#             if i in memo:
#                 return memo[i]
#             for l in wordLen:
#                 if s[i:i+1] in wordDict:
#                     for tail in sentence(s, wordDict, wordLen, i + l, memo):
#                         mem
            memo[i] = [s[i:i + l] + (tail and ' ' + tail) for l in wordLen if s[i:i + l] in wordDict for tail in sentence(s, wordDict, wordLen, i + l, memo)]
#             return memo[i]
#
#         wordDict = set(wordDict)
#         wordLen = set([len(word) for word in wordDict])
#         memo = {}
#         memo[len(s)] = ['']
#         return sentence(s, wordDict, wordLen, 0, memo)

l = []
for i in range(10):
    if i != 1:
        for j in range(20):
            if j != 2:
                l.append(j)
print(l)

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """

        def sentence(s, wordDict, wordLen, i, memo):
            if i in memo:
                return memo[i]
            memo[i] = [s[i:i + l] + (tail and ' ' + tail) for l in wordLen if s[i:i + l] in wordDict for tail in
                       sentence(s, wordDict, wordLen, i + l, memo)]
            return memo[i]

        wordDict = set(wordDict)
        wordLen = set([len(word) for word in wordDict])
        memo = {}
        memo[len(s)] = ['']
        return sentence(s, wordDict, wordLen, 0, memo)