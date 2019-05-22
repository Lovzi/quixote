def quick_sort(A,start,end):
    if start >= end:
        return
    index = position(A,start, end)
    quick_sort(A, start, index-1)
    quick_sort(A, index-1, end)


def position(A,left,right):
    key = A[left]
    while left < right:
        while left < right and key >= A[left]:
            left += 1
        while left < right and key <= A[right]:
            right -= 1
        A[left], A[right] = A[right], A[left]
    return left


if __name__ == '__main__':
    nums=[4,5,7,5,4,8,2,1,9,10]
    print(quick_sort(nums,0,9))