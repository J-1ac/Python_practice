def isprime(n):
    if n==1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

m, n=map(int,input().split())
numlist=list(range(m,n+1))
primenum=0
for i in range(len(numlist)):
    if isprime(numlist[i]):
        print(numlist[i])