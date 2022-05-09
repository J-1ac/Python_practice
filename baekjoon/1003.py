def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)

T = int(input())
result = []
c0, c1 = 0, 0
for _ in range(T):
    
    print(c0, c1)