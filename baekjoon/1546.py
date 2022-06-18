def findmax(testcase):
    max=0
    for i in range(len(testcase)):
        if max<testcase[i]:
            max=testcase[i]
    return max

T = int(input())
case = list(map(int,input().split()))
max = findmax(case)
sum=0
for i in range(len(case)):
    sum += case[i]/max*100
print(sum/T)