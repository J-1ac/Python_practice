T = int(input())
test = list(map(int,input().split()))
max=-1000000
min=1000000
for i in range(T):
    if max<test[i]:
        max=test[i]
    if min>test[i]:
        min=test[i]
print(min,max)