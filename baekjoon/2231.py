n=int(input())
min=n
for i in range(n,0,-1):
    digit=0
    generator=i
    for j in range(len(str(i))):
        digit+=int(str(i)[j])
    if generator+digit==n:
        min=generator
if min==n:
    print("0")
else:
    print(min)