import sys
c0=[1,0]
c1=[0,1]
def fibonacci(n):
    length=len(c0)
    for i in range(length,n+1):
        c0.append(c0[i-2]+c0[i-1])
        c1.append(c1[i-2]+c1[i-1])
    print(c0[n], c1[n])

T = int(sys.stdin.readline())
for _ in range(T):
    n=int(sys.stdin.readline())
    if n==0:
        print("1 0")
    elif n==1:
        print("0 1")
    else:
        fibonacci(n)