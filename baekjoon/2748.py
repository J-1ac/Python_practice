#fibonacci by dynamic programming
import sys

def fibonacci(n):
    memo=[0,1]
    if n<2:
        return memo[n]
    else:
        for i in range(2,n+1):
            memo.append(memo[i-2]+memo[i-1])
        return memo[n]

n=int(sys.stdin.readline())
print(fibonacci(n))