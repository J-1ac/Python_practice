from collections import Counter
import sys
N=int(sys.stdin.readline())
numlist=[]
for _ in range(N):
    numlist.append(int(sys.stdin.readline()))
numlist.sort()
sum=0
for i in range(N):
    sum+=numlist[i]
print(round(sum/N))
print(numlist[(N-1)//2])
cnt=Counter(numlist)
mode=cnt.most_common(2)
if N!=1:
    if mode[0][1] == mode[1][1]:
        print(mode[1][0])
    else:
        print(mode[0][0])
    print(numlist[N-1]-numlist[0])
else:
    print(numlist[0])
    print(0)