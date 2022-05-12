def josephus(peoplelist, k, initial):
    popindex = k-1+initial
    if popindex > len(peoplelist):
        popindex -= len(peoplelist)
    poped = peoplelist[popindex]
    peoplelist.pop[popindex]


N, K = map(int, input().split())
plist=[]
popedlist=[]
for i in range(N):
    plist.append(i+1)
i = 0
while len(popedlist)<N:
    popindex = K+i-1
    while popindex>=len(plist):
        popindex-=len(plist)
    popedlist.append(plist[popindex])
    i=popindex
    plist.pop(popindex)

if len(popedlist)==1:
    print(f"<{popedlist[0]}>")
else:
    for i in range(len(popedlist)):
        if i==0:
            print(f"<{popedlist[0]}", end =", ")
        elif i<len(popedlist)-1:
            print(popedlist[i], end=", ")
        else:
            print(f"{popedlist[i]}>")
