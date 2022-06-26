C = int(input())
for _ in range(C):
    test=list(map(int,input().split()))
    sum, average, count=0,0.0,0
    for i in range(1,test[0]+1):
        sum+=test[i]
    average=sum/test[0]
    for i in range(1,test[0]+1):
        if test[i]>average:
            count+=1
    print(f"{format(count/test[0]*100,'.3f')}%")