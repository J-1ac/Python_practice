T = int(input())
for _ in range(T):
    p=[]
    s=list(input().split())
    for i in range(len(s[1])):
        p.append(s[1][i]*int(s[0]))
    for i in range(len(p)):
        if i!=len(p)-1:
            print(p[i],end="")
        else:
            print(p[i])