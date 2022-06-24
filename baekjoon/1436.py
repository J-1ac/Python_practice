import sys

n=int(sys.stdin.readline())
count=0
i=665
answer=str(666)

while count!=n:
    case=str(i)
    if answer in case:
        count+=1
        i+=1
    else:
        i+=1
print(case)