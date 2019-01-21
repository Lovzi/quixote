"""
    使用深搜，过滤掉重复的
"""

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        self.nums = sorted(nums)
        self.nums_length = len(nums)
        self.vis = [False for i in range(self.nums_length)]
        self.lists = []
        self.ans = []
        self.dfs(0)
        return self.ans

    def dfs(self, n):
        if n >= self.nums_length:
            self.ans.append(self.lists[:])
            return
        for i in range(self.nums_length):
            if i > 0 and self.nums[i] == self.nums[i-1] and not self.vis[i-1]:
                continue
            if not self.vis[i]:
                self.vis[i] = True
                self.lists.append(self.nums[i])
                self.dfs(n+1)
                self.vis[i] = False
                self.lists.pop()

s = Solution()
print s.permuteUnique([3,3,0,3])
