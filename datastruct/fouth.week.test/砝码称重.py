#使用1，3，9，27，。。。。的砝码称重，给定n,请选择合适的砝码方案，每个砝码只能选一次
def get_three_decimal(n):
    strs=""
    while n>0:
        strs+=str(n%3)
        n = n // 3
    return strs[::-1]
def deal_with(s):
    l=[int(i) for i in s[::-1]]
    for i in range(len(l)):
        if l[i] == 2:
            if i+1 < len(l):
                l[i+1] += 1
            else:
                l.append(3**(i+1))
            l[i] = -(3 ** i)
        elif l[i] == 1:
            l[i] = (3 ** i)
    return ''.join([str(i) for i in l[::-1] if i != 0])

if __name__ == '__main__':
    print(deal_with(get_three_decimal(10)),sep="")

