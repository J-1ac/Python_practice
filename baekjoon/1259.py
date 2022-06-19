while True:
    n=int(input())
    if n==0:
        break
    s=str(n)
    newn=0
    for i in range(0,len(s)):
        newn += int(s[i]) * (10 ** i)
    if n==newn:
        print("yes")
    else:
        print("no")