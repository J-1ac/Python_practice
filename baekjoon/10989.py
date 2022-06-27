import sys 

n=int(sys.stdin.readline())
if n<10000:
    numlist=[]
    for _ in range(n):
        numlist.append(int(sys.stdin.readline()))
    numlist.sort()
    for i in range(n):
        print(numlist[i])
else:
    numlist=[0 for i in range(10000)]
    for _ in range(n):
        numlist[int(sys.stdin.readline())-1]+=1
    for i in range(10000):
        for j in range(numlist[i]):
            print(i+1)