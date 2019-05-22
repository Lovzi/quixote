def insert_sort(arr,start=None,count=None):
    if start is None:
        start=0
        count=len(arr)
    elif start is not None and count is None:
        count=start
        start=0
    for pos in range(start+1,count+start):
        temp=arr[pos]
        p=pos-1
        while p>=start:
            if temp<arr[p]:
                arr[p+1]=arr[p]
                p-=1
            else:
                break
        arr[p+1]=temp
    return arr

if __name__ == '__main__':
    nums=[4,5,7,5,4,8,2,1,9,10]
    nums=insert_sort(nums,2,3)
    print(nums)