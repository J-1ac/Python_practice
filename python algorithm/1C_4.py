# 함수 내부&외부에서 정의한 변수와 객체의 식별 번호를 출력하기

n = 1

def put_id():
    x=1
    print(f"id(x) = {id(x)}")

print(f"id(1) = {id(1)}")
print(f"id(n) = {id(n)}")
put_id()

# 파이썬에서 변수는 값을 가지지 않고, 리터럴 자체를 참조한다.