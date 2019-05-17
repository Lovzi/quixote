# def match(s,p):
#     i=0
#     j=0
#     while i<len(s) and j<len(p):
#         if j<0 or s[i] == p[j]:
#             j += 1
#             i += 1
#         else:
#             j=next[j]
#     return i-j if j == len(p) else -1
def match2(s,p):
    i=0
    j=0
    ans=0
    while i<=len(s):
        if j==len(p):
            j=0
            ans += 1
            i -= 1
        elif i < len(s):
            if j<0 or s[i] == p[j]:
                j += 1
                i += 1
            else:
                j=next[j]
        else:
            break
    return ans
def get_next(p):      #得到next数组。
    #next数组定义为当j和i不匹配时，j应该在哪个位置和i重新进行比较。
    next_local = [0]*len(p)
    next_local[0] = -1
    i = 0
    k = next_local[i]
    while i < len(p)-1:
        if k == -1 or p[i] == p[k]:        #假设已经知道了next[i]数组,如果知道了p[j]==p[k]。那么前缀的长度会加1
            ## 注：next数组会刨去当前的元素。
            next_local[i+1] = k+1
            k += 1
            i += 1
        else:
            k = next_local[k]
    return next_local
if __name__  ==  '__main__' :
    num=int(input())
    for i in range(num):
        p=input()
        s=input()
        next = get_next(p)
        print(match2(s, p))
