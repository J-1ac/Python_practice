numlist=[]
isalready=[]
for _ in range(10):
    numlist.append(int(input()))
for i in range(10):
    if numlist[i]%42 not in isalready:
        isalready.append(numlist[i]%42)
print(len(isalready))