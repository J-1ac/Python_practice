def factorial(n):
    result=1
    for i in range(n, 0, -1):
        result*=i
    return result

n, k = map(int, input().split())
j = n-k
print(factorial(n) // (factorial(k) * factorial(j)))