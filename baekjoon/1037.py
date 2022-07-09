n=int(input())
nlist=list(map(int,input().split()))
nlist.sort()
if n==1:
    print(nlist[0]**2)
else:
    print(nlist[0]*nlist[n-1])