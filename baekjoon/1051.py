N, M = map(int, input().split())

rect=[]
for _ in range(N):
    rect.append(list(input()))              # 이차원배열 입력

for k in range(N):
    for i in range(M-1):
        for j in range(M-i-1):
            if rect[k][i] == rect[k][j]:
                d = abs(i-j)                        #유추되는 정사각형 한변의 길이
                if rect[k][i] == rect[k+d][i] and rect[k+d][i] == [k+d][i+d] and ans < d:
                    ans = d