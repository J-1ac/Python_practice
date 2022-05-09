

lenA, lenB = map(int, input().split())

A = []*lenA
B = []*lenB

A = list(map(int, input().split(" ")))
B = list(map(int, input().split(" ")))

A.extend(B)

for i in range(len(A)-1):
    for j in range(len(A)-i-1):
        if A[j] > A[j+1]:
            A[j], A[j+1] = A[j+1], A[j]

print(quick_sort(A))