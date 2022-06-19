T = int(input())
for _ in range(T):
    test=input()
    score=0
    bonus=0
    if test[0]=="O":
        score+=1
        bonus+=1
    for i in range(1,len(test)):  
        if test[i]=="O":
            score+=(1+bonus)
            bonus+=1
        if test[i]=="X":
            bonus=0
    print(score)