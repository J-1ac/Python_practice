def isprime(n):
    if n==1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

n=int(input())
numlist=list(map(int,input().split()))
primenum=0
for i in range(n):
    if isprime(numlist[i]):
        primenum+=1
print(primenum)