n,k=map(int, input().split())
list1=list(map(int,input().split()))
list2=list(map(int,input().split()))
newlist=list1+list2
newlist.sort()
print(*newlist)