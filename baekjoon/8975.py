n=int(input())
answer=[]
checklist=[]
for _ in range(n):
    answer.append(input())
m=int(input())
count=0
if n%2==0:
    min=n//2
else:
    min=n//2+1
for _ in range(m):
    checklist.append(input())
for i in range(len(checklist)):
    if checklist[i] in answer:
        answer.remove(checklist[i])
        count+=1
    if count==min:
        break
print(i+1)