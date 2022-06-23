from collections import deque
import sys

n=int(sys.stdin.readline())
mydeque = deque()
for _ in range(n):
    order=list(sys.stdin.readline().split())
    if order[0]=="push_front":
        mydeque.appendleft(order[1])
    elif order[0]=="push_back":
        mydeque.append(order[1])
    elif order[0]=="pop_front":
        if mydeque:
            print(mydeque.popleft())
        else:
            print("-1")
    elif order[0]=="pop_back":
        if mydeque:
            print(mydeque.pop())
        else:
            print("-1")
    elif order[0]=="size":
        print(len(mydeque))
    elif order[0]=="empty":
        if mydeque:
            print("0")
        else:
            print("1")
    elif order[0]=="front":
        if mydeque:
            print(mydeque[0])
        else:
            print("-1")
    elif order[0]=="back":
        if mydeque:
            print(mydeque[len(mydeque)-1])
        else:
            print("-1")