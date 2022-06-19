n, x=map(int, input().split())
num = list(map(int, input().split()))
underx=[]
for i in range(n):
    if num[i]<x:
        underx.append(num[i])
print(*underx)