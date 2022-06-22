n=int(input())
plist=[]
for _ in range(n):
    plist.append(list(input().split()))
for i in range(n):
    plist[i][0]=int(plist[i][0])
plist.sort(key=lambda x:x[0])
for i in range(n):
    print(*plist[i])