class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n_len = len(nums)
        count = [0 for i in range(n_len)]
        for i in range(n_len-2, -1, -1):
            j = i + 1
            while j < n_len and nums[i] <= nums[j]:
                j += 1
            if j == n_len:
                count[i] = 0
            else:
                count[i] = count[j] + 1
        return count

s = Solution()
print(s.countSmaller([5,2,6,1]))