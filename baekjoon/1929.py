import sys

m, n=map(int,sys.stdin.readline().split())
numlist=list(range(m,n+1))
primenumlist=[True]*len(numlist)
for i in range(len(numlist)):
    isprimenum=True
    if numlist[i]==1:
        primenumlist[i]=False
        continue
    elif primenumlist[i]==True:
        for j in range(2,int(numlist[i]**(1/2)+1)):
            if numlist[i]%j==0:
                isprimenum=False
                primenumlist[i]=False
                break
        if isprimenum:
            for k in range(numlist[i]*2-m,len(numlist),numlist[i]):
                primenumlist[k]=False
    else:
        continue
for i in range(len(numlist)):
    if primenumlist[i]:
        print(numlist[i])