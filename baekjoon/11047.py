def cal(K, coinlist):
    count=0
    for i in range(len(coinlist)-1,0,-1):
        while K>=coinlist[i]:
            print(K, coinlist[i])
            K-=int(coinlist[i])
            print(count)
            count+=1
    return print(count)

T, K = map(int, input().split())
coin=[]
for i in range(T):
    coin.append(int(input()))
cal(K, coin)


"""
가장 작은 coin이 남은 K를 나눌수 없는경우 오류 발생
"""