T=int(input())
for _ in range(T):
    x1, y1, x2, y2 = map(int,input().split())
    n=int(input())
    count=0
    for _ in range(n):
        cx, cy, r = map(int, input().split())
        if (cx-x1)**2+(cy-y1)**2<r**2 and (cx-x2)**2+(cy-y2)**2<r**2:
            continue
        elif (cx-x1)**2+(cy-y1)**2<r**2:
            count+=1
        elif (cx-x2)**2+(cy-y2)**2<r**2:
            count+=1
    print(count)