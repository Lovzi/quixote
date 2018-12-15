# class Solution(object):
#     def makesquare(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         sums=sum(nums)
#         num_len=len(nums)
#         if sums % 4 != 0:
#             return False
#         length = sums / 4
#         if any(map(lambda x:x>length,nums)):
#             return False
#         vis=[False]*len(nums)
#         state=[0, 0, 0, 0]
#         def dfs(n,vis,state,cur):
#             if n>=num_len or cur>=4:
#                 if all(map(lambda x:x==length,state)):
#                     return True
#                 else:
#                     return False
#             for i in range(num_len):
#                 if not vis[i]:
#                     vis[i] = True
#                     if state[cur]+nums[i] < length:
#                         state[cur] += nums[i]
#                         return dfs(n+1,vis,state,cur)
#                         state[cur] -= nums[i]
#                     elif state[cur]+nums[i] == length:
#                         state[cur] += nums[i]
#                         cur += 1
#                         return dfs(n + 1, vis, state, cur)
#                         state[cur] -= nums[i]
#                     vis[i] = False
#         return dfs(0, vis, state, 0)
# s=Solution()
# print(s.makesquare([3,3,3,3,4]))
# print(s.makesquare([1,1,1,1,3,3,3,3]))




# class MinStack(object):
#
#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.data = []
#         self.min = []
#
#     def push(self, x):
#         """
#         :type x: int
#         :rtype: void
#         """
#         self.data.append(x)
#         if self.min == [] or x < self.data[self.min[-1]]:
#             self.min.append(len(self.data)-1)
#     def pop(self):
#         """
#         :rtype: void
#         """
#         if self.data.pop() == self.getMin():
#             self.min.pop()
#
#
#     def top(self):
#         """
#         :rtype: int
#         """
#         return self.data[-1]
#
#     def getMin(self):
#         """
#         :rtype: int
#         """
#         return self.data[self.min[-1]]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


# class Solution(object):
#     def isNumber(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         flag = True
#         s = '0' + s.strip()
#         print(s)
#         try:
#             float(s)
#             return True
#         except:
#             spp = s.split('E')
#             sp = s.split('e')
#             if len(spp) == 2:
#                 try:
#                     float(spp[0])
#                     float(spp[1])
#                     return True
#                 except:
#                     return False
#             if len(sp) == 2:
#                 try:
#                     float(sp[0])
#                     float(sp[1])
#                     return True
#                 except:
#                     return False
#             return False
# s = Solution()
# print(s.isNumber('.1'))

# import os
#
# # path = os.path.abspath(__file__)
# lists = []
# def getPath(pathdir):
#     paths = os.listdir(pathdir)
#     for i in range(len(paths)):
#         path = os.path.join(pathdir, paths[i])
#         if os.path.isfile(path):
#             lists.append(path)
#         else:
#             getPath(path)
#     return lists
# l = getPath('/home/tarena/桌面/algorithm')
# for i in l:
#     print(i)



# class Solution(object):
#     def minSubArrayLen(self, s, nums):
#         """
#         :type s: int
#         :type nums: List[int]
#         :rtype: int
#         """
#         left = 0
#         right = 0
#         max_length = 99999999999
#         is_series = False
#         while right < len(nums):
#             if sum(nums[left:right+1]) < s:
#                 right += 1
#             else:
#                 sums = sum(nums[left:right + 1])
#                 while left <= right and sums >= s:
#                     if max_length > right - left + 1:
#                         max_length = right - left + 1
#                     left += 1
#                     sums = sum(nums[left:right + 1])
#                 right += 1
#         return 0 if max_length == 99999999999 else max_length
# s =Solution()
# print(s.minSubArrayLen(10, [5,1,1,1,1,1,7]))
#

# 分析 'ababbcde' = 'aba bb c d e'

# class Solution:
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         left = [[0,0] for _ in range(len(prices))]
#         right = [[0,0] for _ in range(len(prices))]
#
#         def get_price(prices):
#             if len(prices) < 2:
#                 return 0
#             price = 0
#             min_num = prices[0]
#             for i in prices:
#                 min_num = min(i, min_num)
#                 price = max(i - min_num, price)
#             return price
#
#         price = 0
#         for i in range(len(prices)):
#             price = max(price, get_price(prices[0:i]) + get_price(prices[i:len(prices)]))
#         return price
# s = Solution()
# print(s.maxProfit([3,3,5,0,0,3,1,4]))
# print(s.maxProfit([1,2,3,4,5]))
# print(s.maxProfit([7,6,4,3,1]))


class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        row_length = len(grid)
        col_length = len(grid[0])
        def is_map(i, j):
            return 0 <= i < row_length and 0 <= j < col_length
        def dfs(i, j):
            if not is_map(i, j):
                return
            if grid[i][j] != '1' or vis[i][j]:
                return
            vis[i][j] = True
            for direct in direction:
                dfs(i+direct[0], j+direct[1])
        direction = [(-1, 0), (0, 1), (1, 0), (0,-1)]
        vis = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and not vis[i][j]:
                    res += 1
                    dfs(i, j)
        return res
s = Solution()
print(s.numIslands([["1","1","1"],["0","1","0"],["1","1","1"]]))



