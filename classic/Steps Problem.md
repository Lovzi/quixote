## 台阶问题

一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

### 斐波那契思想
```python
a, b, n = 1, 2, 39

for i in range(3, n+1):
    a, b = b, a+b
print(b)
```


### 递归思想
```python
fib = lambda n: n if n <= 2 else fib(n - 1) + fib(n - 2)
```

### dp思想
```python
def f(n, dp):
    if n <= 2:
        return n
    else:
        if n in dp:
            return dp[n]
        else:
            dp[n] = f(n-1, dp) + f(n-2, dp)
            return dp[n]

print(f(39, {}))
```

