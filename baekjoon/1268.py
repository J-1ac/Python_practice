n=int(input())
studentinfo=[]
for _ in range(n):
    studentinfo.append(list(map(int,input().split())))
studentpoint=[0]*n
for t in range(5):
    for i in range(n-1):
        for j in range(i+1,n):
            if studentinfo[i][t]==studentinfo[j][t]:
                studentpoint[i]+=1
                studentpoint[j]+=1
max=0
studentnum=0
print(studentpoint)
for i in range(n):
    if max<studentpoint[i]:
        max=studentpoint[i]
        studentnum=i+1
print(studentnum)