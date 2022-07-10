n=int(input())
moneystack=[]
for _ in range(n):
    money=int(input())
    if money!=0:
        moneystack.append(money)
    else:
        moneystack.pop()
sum=0
for i in range(len(moneystack)):
    sum+=moneystack[i]
print(sum)