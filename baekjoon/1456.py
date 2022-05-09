def is_prime_number(N):
    if N == 1:
        return False
    for i in range(2, N):
        if N % i == 0:
            return False

A, B = map(int, input().split(" "))
count = 0
print(A, B)
for i in range(A, B):
    if is_prime_number(i):
        print(f"find prime number: {i}")
        j=2
        while pow(i, j) <= B:
            count += 1
            j += 1
print(count)
