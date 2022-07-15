a,b=map(int,input().split())
numlist=[]
sum=0
for i in range(45):
    for j in range(i+1):
        numlist.append(i+1)
for i in range(a-1,b):
    sum+=numlist[i]
print(sum)