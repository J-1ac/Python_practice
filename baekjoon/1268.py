n=int(input())
studentinfo=[]
studentpoint=[0]*n
max=0
studentnum=1
for i in range(n):
    studentinfo.append(list(map(int,input().split())))
    studentpoint[i]=[0]*n

for t in range(5):
    for i in range(n-1):
        for j in range(i+1,n):
            if studentinfo[i][t]==studentinfo[j][t]:
                studentpoint[i][j]=1
                studentpoint[j][i]=1
cnt=[]
for l in studentpoint:
    cnt.append(l.count(1))
for i in range(n):
    if max<cnt[i]:
        max=cnt[i]
        studentnum=i+1
print(studentnum)