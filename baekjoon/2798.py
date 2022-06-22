import sys

n, m = map(int,sys.stdin.readline().split())
cards=list(map(int,(sys.stdin.readline().strip().split())))
mindifference=m
difference=0
for i in range(n-2):
    for j in range(1+i, n-1):
        for k in range(1+j, n):
            sum=cards[i]+cards[j]+cards[k]
            if sum>m:
                continue
            else:
                difference=m-sum
                if difference<mindifference:
                    mindifference=difference
print(m-mindifference)