# +와 -를 번갈아 출력하기 2

print("+와 -를 번갈아 출력합니다.")
n = int(input("몇 개를 출력할까요?: "))

for _ in range(n//2):                   #for문에 _사용 -> 반환하는 값 사용 x, 무시하고 싶은 값 _로 표현 가능
    print("+-", end="")

if n % 2:
    print("+", end="")

print()