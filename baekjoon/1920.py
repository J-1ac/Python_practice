import sys

def binary_search(target, data):
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2
        if data[mid] == target:
            return print("1")
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid -1
    return print("0")

n=int(input())
alist=list(sys.stdin.readline().split())
m=int(input())
findlist=list(sys.stdin.readline().split())
alist.sort()
for i in range(m):
    binary_search(findlist[i], alist)