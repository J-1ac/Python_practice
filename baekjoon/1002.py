import math

def cal(info):
    x1, y1, r1, x2, y2, r2 = info[0], info[1], info[2], info[3], info[4], info[5]

    d = math.sqrt(math.pow(x1-x2, 2)+math.pow(y1-y2, 2))
    r = r1 + r2

    if d == 0:                                              # 예외처리
        if (r1==r2):                                        # 동일한 원인 경우 -> 무수히 많은 접점
            return -1
        else:
            return 0                                        # 동심원인 경우 -> 접점 없음
    elif d == r or d == abs(r1-r2):                         # 내접원, 외접원
        return 1
    elif d > r or d < abs(r1-r2):                                             
        return 0
    else:
        return 2


T = int(input())            # 테스트 케이스 수 입력
result = [] * 3
for _ in range(T):
    information = list(map(int, input().split()))
    result.append(cal(information))

for i in range(len(result)):
    print(result[i])