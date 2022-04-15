# 1~12까지 8을 건너뛰고 출력하기 1

for i in range(1,13):
    if i ==8:                       # 건너뛰는 판단을 매번함 -> 비효율적
        continue
    print(i, end=" ")

print()