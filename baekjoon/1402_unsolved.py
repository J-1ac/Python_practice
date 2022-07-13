import sys
T=int(sys.stdin.readline())
for _ in range(T):
    a,b=map(int,sys.stdin.readline().split())
    ispossible=False
    for i in range(1,int((a**(1/2))+1)):
        if a%i==0:
            if b==i+(a//i):
                ispossible=True
                break
    if ispossible:
        print("yes")
    else:
        print("no")