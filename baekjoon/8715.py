n=int(input())
numlist=list(map(int,input().split()))
numlist.sort()
ispermutation=True
for i in range(n):
    if i+1!=numlist[i]:
        ispermutation=False
if ispermutation:
    print("TAK")
else:
    print("NIE")