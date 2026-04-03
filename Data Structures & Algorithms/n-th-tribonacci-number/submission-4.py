class Solution:
    def tribonacci(self, n: int) -> int:
        series=[]
        if n==0:
            return 0
        if n==1:
            return 1
        if n-1<=2:
            return n-1
        a=0
        b=0
        c=1
        for _ in range(n-1):
            a,b,c=b,c,a+b+c
        return c

