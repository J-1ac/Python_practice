n=int(input())
count=0
ispossible=True
while n%5!=0 and n>0:
    n-=3
    count+=1
if n%5!=0 and n!=0:
    ispossible=False
while n>0:
    n-=5
    count+=1
if ispossible:
    print(count)
else:
    print("-1")