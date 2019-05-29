def count_sort_with_list(nums):
    """
        思想是以空间换时间，创建一个数组，数组的长度是数组的最大值。
    :param nums: 待排序数组
    :return: 排序后的数组
    """
    max_num = max(nums)
    tmp = [0] * (max_num+1)
    print(len(tmp))
    for v in nums:
        tmp[v] += 1
    new_nums = []
    for v in range(len(tmp)):
        # while tmp[v] > 0:
        #     new_nums.append(v)
        #     tmp[v] -= 1
        if tmp[v] > 0:
            new_nums.extend([v] * tmp[v])
    return new_nums


def count_sort_with_dict(nums):
    """
        目标是使用dict来减少空间的浪费，数组的长度是数组的最大值。
    :param nums: 待排序数组
    :return: 排序后的数组
    """
    tmp = {}
    for v in nums:
        tmp[v] = tmp.get(v, 0) + 1
    new_nums = []
    max_num = max(tmp)
    print(len(tmp))
    for v in range(max_num+1):
        # while tmp[v] > 0:
        #     new_nums.append(v)
        #     tmp[v] -= 1
        if v in tmp:
            new_nums.extend([v] * tmp[v])
    return new_nums





import random
import time
t1 = time.time()
print(count_sort_with_list([random.randint(1,1000) for i in range(1000)]))
t2 = time.time()
print(count_sort_with_dict([random.randint(1, 1000) for v in range(1000)]))
t3 = time.time()
print(t2-t2)
print(t3-t2)