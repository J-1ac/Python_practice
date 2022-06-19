a, b = map(str, input().split())
newa=0
newb=0
for i in range (3):
    newa += int(a[i]) * (10**(i))
    newb += int(b[i]) * (10**(i))
if newa>newb:
    print(newa)
else:
    print(newb)