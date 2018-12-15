def select_sort(arr,start=None,count=None):
    if start is None:
        start=0
        count=len(arr)
    elif start is not None and count is None:
        count=start
        start=0
    for i in range(start,count+start-1):
        min_num=i
        for j in range(i,count+start):
            min_num=min_num if arr[min_num]<arr[j] else j
        arr[i],arr[min_num]=arr[min_num],arr[i]
    return arr
if __name__ == '__main__':
    nums=[4,5,7,5,4,8,2,1,9,10]
    nums=select_sort(nums,10)
    print(nums)