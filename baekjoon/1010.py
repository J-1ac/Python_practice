def combination(N, M):
    numerator = 1
    denominator = 1
    for i in range(1, N+1):
        numerator *= (M-i+1)
        denominator *= i
    return int(numerator / denominator)

T = int(input())
for _ in range(T):
    N, M = map(int, input().split(" "))
    print(combination(N,M))