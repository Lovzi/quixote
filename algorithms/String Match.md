###kmp
```python
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

```


###Rabinkarp(滚动hash)
通过计算每个n大小的字符串计算其hash值，然后匹配其hsah只需要O(1)的时间复杂度。

但是由于预处理的时间为(O(m * n))， 所以还需要进行优化。

后来有位大牛提出了一个滚动hash的优化思路。其实就是在计算第一个hash源字符串之后，向前推进一位的同时，扣除最后一位，得到新的字符串
hash值，这样在预处理字符串的hash值只需要O(m + n), m是源字符串所花费的时间，n是匹配字符串所花费的时间。最后进行m次比较hash值则可以找出所有匹配的字符串位置
```python
def get_hash(s,n):
    res=[]   #存储hash值
    temp=ord(s[0])
    seed=31
    for i in range(1,n):
        temp=(temp)*seed+ord(s[i])      #存储第一个n长字符串的hash值
    res.append(temp)
    for i in range(n,len(s)): #进行滚动hash。每前进一个字符，就扣掉扣掉最后一个字符。
        #即等于加上新字符并乘以seed，然后减去老字符*seed**n
        res.append(((res[i-n]*seed)+ord(s[i])-ord(s[i-n])*seed**n))
    print(res)
    return res
def match(hash1,hash2,n,s,p):
    for i,h in enumerate(hash1):
        if h==hash2:
            k=0
            for j in range(i,i+n):
                if s[j]!=p[k]:
                    return -1
                else:
                    return i
    return -1


if __name__ == '__main__':
    s='ABABABA'
    p='ABA'
    hash1=get_hash(s,len(p))
    hash2=get_hash(p,len(p))[0]
    index=match(hash1,hash2,len(p),s,p)
    print(index)
#


# print(2030717*31+ord('A')-ord('B')*31**3)
print(ord('A')*31**2+ord('B')*31**1+ord('A'))
```