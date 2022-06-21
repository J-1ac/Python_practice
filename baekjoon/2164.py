import sys
from collections import deque

n=int(sys.stdin.readline())
cards=[]
for i in range(n):
    cards.append(i+1)
cardqueue = deque(cards)
while len(cardqueue)>1:
    cardqueue.popleft()
    cardqueue.append(cardqueue[0])
    cardqueue.popleft()
print(*cardqueue)