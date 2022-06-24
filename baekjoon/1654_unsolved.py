import sys

k,n=map(int,sys.stdin.readline().split())
originlines=[]
for _ in range(k):
    originlines.append(int(sys.stdin.readline()))
originlines.sort(reverse=True)

left=1
right=originlines[0]-1
while left<right:
    mid = left+right//2
    count=0
    for i in range(len(originlines)):
        count+=originlines[i]//mid
    if count>=n:
        left=mid+1
    else:
        right=mid-1

print(left)


#이진탐색 최댓값 구하기