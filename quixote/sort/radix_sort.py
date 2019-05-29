def radix_sort(arr):
    radix=[[] for _ in range(11)]
    max_num=max(arr)
    bit=0
    while max_num>0:
        bit+=1
        max_num//=10
    for b in range(1,bit+1):
        for a in arr:
            temp=a//10**(b-1)
            radix[temp%10].append(a)
        i=0
        for r in radix:
            for j in range(len(r)):
                arr[i]=r[j]
                i+=1
            else:
                r.clear()
    return arr
if __name__ == '__main__':
    # nums=[4,5,7,5,4,8,2,1,9,5]
    import random
    nums1=list(range(1000000,0,-1))
    nums2=nums1[:]
    nums3=nums2[:]
