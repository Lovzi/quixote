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