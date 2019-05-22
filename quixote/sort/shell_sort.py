def shell_sort(arr):
    d=4
    while d>0:
        for i in range(0,d):
            pos=d+i
            while pos < len(arr):
                temp = arr[pos]
                p = pos - d
                while p >= 0:
                    if temp < arr[p]:
                        arr[p + d] = arr[p]
                        p -= d
                    else:
                        break
                arr[p + d] = temp
                pos += d
        d//=2
    return arr
if __name__ == '__main__':
    # nums=[4,5,7,5,4,8,2,1,9,10]
    # print(shell_sort(nums))
    nums1=list(range(10000,0,-1))
    nums2=nums1[:]
    nums3=nums2[:]
    import time
    t1=time.time()
    shell_sort(nums1)
    t2=time.time()
    print(t2-t1)
    nums2.sort()
    t3=time.time()
    print(t3-t2)
    import select_sort
    select_sort.select_sort(nums3)
    print(time.time()-t3)







