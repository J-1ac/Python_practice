T=int(input())
points=[]
for _ in range(T):
    points.append(list(map(int, input().split())))
points.sort(key=lambda x :(x[1],x[0]))
for i in range(T):
    print(*points[i])