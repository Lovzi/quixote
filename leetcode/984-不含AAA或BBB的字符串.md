```cython
class Solution(object):
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        res = ""
        a, b = "a", "b"
        if A == B:
            return (a + b) * A
        if B > A:
            A, B = B, A
            a, b = b, a
        while A and B:
            if (A > B):
                res += a * 2 + b
                A -= 2
                B -= 1
            else:
                res += a + b
                A -= 1
                B -= 1
        if A:
            res += a * A
        if B:
            res += b * B

        return res
s = Solution()
print s.strWithout3a3b(3,4)
```


# 分析

将数字分段进行填充，每次填充2个b,一个a或者两个a一个b




