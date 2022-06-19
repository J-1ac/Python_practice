testcase=[]
max=0
maxcount=0
for _ in range(9):
    testcase.append(int(input()))
for i in range(9):
    if max<testcase[i]:
        max=testcase[i]
        maxcount=i+1
print(max)
print(maxcount)