n=int(input())
init=n
count=0

if n<10:
    n*=11
else:
    sumn=n//10+n%10
    if sumn>=10:
        n=sumn%10+(n%10)*10
    else:
        n=sumn+(n%10)*10 
count+=1
while n!=init:
    if n<10:
        n*=11
    else:
        sumn=n//10+n%10
        if sumn>=10:
            n=sumn%10+(n%10)*10
        else:
            n=sumn+(n%10)*10
    count+=1

print(count)