import sys
T, K = map(int, sys.stdin.readline().split())
coin=[]
for i in range(T):
    coin.append(int(sys.stdin.readline()))
count=0
for i in range(len(coin)-1,-1,-1):
    while K>=coin[i]:
        count+=K//coin[i]
        K=K%coin[i]
print(count)