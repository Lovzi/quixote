##排序算法

### 1.快速排序(Quick Sort) 
#### 分析
快速排序的思路主要是划分

确立一个主元，然后将小于主元的划分到主元的左边，大于主元的划分到主元的右边
```python
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
```

### 2.冒泡排序(Bubble Sort)
```python
def bubble_sort(arr,start=None,count=None):
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
    nums=bubble_sort(nums,2,3)
    print(nums)
```

### 3.计数排序(Count Sort)
一句话:开辟一个辅助空间（原序列最大值+1)，通过辅助空间的索引和原数据绑定

即数据所对应的下标加1(可能存在重复元素)，然后遍历辅助空间，如果下标对应值不为0,则添加对应个数下标的值进入原始空间
```python
def count_sort(A):
    max_num=max(A)
    fuzhu=[0]*(max_num+1)
    for v in A:
        fuzhu[v]+=1
    A.clear()
    for v in range(len(fuzhu)):
       if fuzhu[v]:
           i=fuzhu[v]
           while i>0:
               A.append(v)
               i-=1
    return A
count_sort([10,9,5,10,6,20])
```


### 4.堆排序(Heap Sort)
```python
def create_max_heap(A):
    for i in range(len(A)//2-1,0,-1):
        change_max_heap(A,i,len(A))
def change_max_heap(A,i,n):
    left=2*i+1
    right=2*i+2
    if left>=n:  #如果左孩子越界，则右孩子肯定越界
        return
    if right>=n:  #如果右孩子越界，则孩子节点的最大值为左孩子
        max_index=left
    else:  #否则找到左右孩子节点的最大节点索引
        max_index=left if A[left]>A[right] else right
    if A[i]<A[max_index]:  #如果父节点小于孩子节点，则进行交换，并递归判断
        A[i],A[max_index]=A[max_index],A[i]
        change_max_heap(A,max_index,n)
def heap_sort(A,start=0):
    create_max_heap(A)  #进行堆化
    for i in range(len(A)-1,0,-1):
        A[0],A[i]=A[i],A[0]  #将堆末和堆顶进行交换，然后调整整个堆为大顶堆
        change_max_heap(A,0,i)  #对剩下的数组长度进行判断，调整为大顶堆。
if __name__ == '__main__':
    l = [78, 56, 34, 43, 4, 1, 15, 2, 23]
    print(l)
    heap_sort(l)
    print(l)
```


### Select Sort
```python
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
```


### Insert Sort
```python
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
```


### Radix Sort
```python
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
```


### Shell Sort
```python
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
```