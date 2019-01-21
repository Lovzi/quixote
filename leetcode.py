# from collections import OrderedDict
# class Solution(object):
#     def totalFruit(self, tree):
#         """
#         :type tree: List[int]
#         :rtype: int
#         """
#         cnt = OrderedDict()
#         ans = 0
#         i = 0
#         for j, v in enumerate(tree):
#             cnt[v] = j
#             if cnt[v] > 2:
#                 i = cnt.popitem(0)[1]
#             ans = max(ans, j-i)
#         return ans
#
# if __name__ == '__main__':
#     solu = Solution()
#     tree = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]
#     print(solu.totalFruit(tree))
#
#
# class Solution(object):
#     def numSubarraysWithSum(self, A, S):
#         """
#         :type A: List[int]
#         :type S: int
#         :rtype: int
#         """
#         sums = [0]
#         for v in A:
#             sums.append(sums[-1]+v)
#         left = 0
#         right = 1
#         count = 0
#         sum_len = len(sums)
#         while left < right and right < sum_len:
#             if sums[right] - sums[left] == S:
#                 count += 1
#
#             elif sums[right] - sums[left] < S:
#                 right += 1
#             else:
#
#         return count
# s = Solution()
# print s.numSubarraysWithSum([1,0,1,0,1], 2)


# class Solution(object):
#     def multiply(self, num1, num2):
#         """
#         :type num1: str
#         :type num2: str
#         :rtype: str
#         """
#         tmp = []
#         reverse_num1 = num1[::-1]
#         reverse_num2 = num2[::-1]
#         for i in range(len(reverse_num1)):
#             x = ord(num1[i]) - 48
#             for j in range(len(reverse_num2)):
#                 y = ord(num2[j]) - 48
#                 mul = x * y
#


class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        left = 0
        right = 0
        for c in s:
            if c == '(':
                left += 1
            elif c == ')':
                right += 1
        left, right = left-right, 0 if left > right else 0, right - left

    def DFS(self, s, start, left, right, res):
        if left == right:
            return res.append(s) if self.is_valid(s) else None
        else:
            for i in range(start, len(s)):
                if i != start and s[i] == s[i-1]:
                    continue #重复的只计算一次
                elif left > 0 and s[i] == "(": #左多
                    self.DFS(s[:i]+s[i+1:], i, left-1, right, res)
                elif right > 0 and s[i] == ")": #右多
                    self.DFS(s[:i]+s[i+1:], i, left, right-1, res)

    def is_valid(self, s):
        left = 0
        for c in s:
            if c == '(':
                left += 1
            elif c == ')':
                if left > 0:
                    left -= 1
                else:
                    return False
        return not left
