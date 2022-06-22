import sys
from collections import Counter

n=int(sys.stdin.readline())
nlist=list(map(int, sys.stdin.readline().split()))
nlist.sort()
m=int(sys.stdin.readline())
mlist=list(map(int, sys.stdin.readline().split()))
cnt = Counter(nlist)

for i in range(m):
    if i!=m-1:
        print(cnt[mlist[i]], end=" ")
    else:
        print(cnt[mlist[i]])

""" 이분탐색 실패버전
import sys

n=int(sys.stdin.readline())
nlist=list(map(int, sys.stdin.readline().split()))
nlist.sort()
m=int(sys.stdin.readline())
mlist=list(map(int, sys.stdin.readline().split()))

for i in range(m):
    start = 0
    end = len(nlist)-1
    count=0
    while start <= end:
        mid = (start + end) // 2
        if nlist[mid]==mlist[i]:
            count+=1
            previous=mid-1
            after=mid+1
            while previous>=start and nlist[previous]==mlist[i]:
                count+=1
                previous-=1
            while after<=end and nlist[after]==mlist[i]:
                count+=1
                after+=1
            break
        elif nlist[mid] < mlist[i]:
            start = mid + 1
        else:
            end = mid -1
    print(count, end=" ")
"""