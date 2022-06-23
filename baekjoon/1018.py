n,m=map(int,input().split())
board=[]
for i in range(n):
    board.append(input())
min_change=63

for l in range(n-7):
    for k in range(m-7):
        change1,change2=0,0
        for i in range(l,l+8):
            for j in range(k, k+8):  
                if (i+j)%2==0:
                    if board[i][j]=="W":
                        change1+=1
                    else:
                        change2+=1
                else:
                    if board[i][j]=="B":
                        change1+=1
                    else:
                        change2+=1
        if change1<change2:
            need_change=change1
        else:
            need_change=change2
        if min_change>need_change:
            min_change=need_change
print(min_change)    