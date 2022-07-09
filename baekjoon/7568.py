n=int(input())
plist=[]
for _ in range(n):
    plist.append(list(map(int, input().split())))
ans=[]
for i in range(n):
    k=0
    for j in range(0,i):
        if plist[i][0]<plist[j][0] and plist[i][1]<plist[j][1]:
            k+=1
    for j in range(i+1,n):
        if plist[i][0]<plist[j][0] and plist[i][1]<plist[j][1]:
            k+=1
    ans.append(k+1)
print(*ans)