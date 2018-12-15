# def lowerBound(nums, target):    #寻找大于等于target的最小值，即数组对于目标值的下限
#     if len(nums) == 0 or nums[0] > target:
#         return 0  # LowerBound
#     if nums[-1] < target:
#         return len(nums)
#     left = 0
#     right = len(nums) - 1
#     mid = (left + right) // 2
#     ans = mid
#     while left <= right:
#         if (nums[mid] >= target):
#             ans = mid
#             right -= 1
#         else:
#             left += 1
#         mid = (left + right) // 2
#     return ans
#
#
# def upperBound(nums, target):   #寻找小于等于target的最大值，即数组对于目标值的上限
#     if len(nums) == 0 or nums[0] > target:
#         return 0  # LowerBound
#     if nums[-1] < target:
#         return len(nums)
#     left = 0
#     right = len(nums) - 1
#     mid = left+(right-left) // 2
#     ans = mid
#     while left <= right:
#         if (nums[mid] <= target):
#             ans = mid
#             left += 1
#         else:
#             right -= 1
#         mid = left + (right - left) // 2
#     return ans

