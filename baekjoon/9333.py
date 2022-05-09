T = int(input())
result = []
for _ in range(T):

    R, B, M = map(float, input().split(" "))

    count = 0
    while B > 0.0:
        B = round(B * (100.0+R) / 100.0 + 0.00000000001 , 2)
        B -= M
        count += 1
        if count > 1200:
            break

    if count <= 1200:
        result.append(count)
    else:
        result.append("impossible")

for i in range(len(result)):
    print(result[i])