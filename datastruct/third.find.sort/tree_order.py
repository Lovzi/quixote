#树的遍历
def in_order(lists,n):  #中序
    if n>=len(lists):
        return
    in_order(lists,2*n+1)
    print(lists[n],end=' ')
    in_order(lists,2*n+2)
def front_order(lists,n):  #前序
    if n>=len(lists):
        return
    print(lists[n],end=' ')
    front_order(lists,2*n+1)
    front_order(lists,2*n+2)
def rear_order(lists,n):  #后序
    if n>=len(lists):
        return
    rear_order(lists,2*n+1)
    rear_order(lists,2*n+2)
    print(lists[n],end=' ')
if __name__ == '__main__':
    l=[78, 56, 34, 43, 4, 1, 15, 2, 23]
    in_order(l,0)
    print()
    front_order(l,0)
    print()
    rear_order(l,0)