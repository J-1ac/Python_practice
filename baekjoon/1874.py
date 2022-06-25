import sys
from collections import deque
n=int(sys.stdin.readline())
wanted_numlist=[]
origin_numlist=deque(range(1, n+1))
stack=[]
answer=[]

for i in range(n):
    wanted_numlist.append(int(sys.stdin.readline()))

for i in range(len(wanted_numlist)):
    while len(origin_numlist)!=0 and origin_numlist[0] <= wanted_numlist[i]:
        stack.append(origin_numlist[0])
        origin_numlist.popleft()
        answer.append("+")
    if wanted_numlist[i]!=stack[len(stack)-1]:
        answer="NO"
        break
    else:
        stack.pop()
        answer.append("-") 

if answer=="NO":
    print("NO")
else:
    print('\n'.join(answer))