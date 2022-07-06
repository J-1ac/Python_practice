import sys
n=int(sys.stdin.readline())
if n==1:
    print("1")
else:
    i, count, distance=2, 1, 2
    while i<n:
        if i+(6*count)<=n:
            i=i+(6*count)
            count+=1
            distance+=1
            continue
        else:
            break
    print(distance)