def bubble_sort(arr, start=None, count=None):
    if start is None:
        start=0
        count=len(arr)
    elif start is not None and count is None:
        count=start
        start=0
    for i in range(start,count+start-1):
        for j in range(start,count+start-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

if __name__ == '__main__':
    nums=[4,5,7,5,4,8,2,1,9,5]
    nums=bubble_sort(nums, 2, 3)
    print(nums)


