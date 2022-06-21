T = int(input())
points=[]
for _ in range(T):
    points.append(list(map(int, input().split())))
points.sort()
for i in range(T):
    print(*points[i])