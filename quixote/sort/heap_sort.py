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

