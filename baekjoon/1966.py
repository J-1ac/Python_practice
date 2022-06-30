#우선순위 큐
from collections import deque

T=int(input())
for _ in range(T):
    n,m=map(int, input().split())
    priority=deque(map(int,input().split()))
    index=deque(range(n))
    count=1
    while True:
        isprint=True
        for i in range(1,len(priority)):
            if priority[0]<priority[i]:
                priority.append(priority[0])
                priority.popleft()
                index.append(index[0])
                index.popleft()
                isprint=False
                break
        if isprint:
            if index[0]==m:
                print(count)
                break
            else:
                priority.popleft()
                index.popleft()
                count+=1