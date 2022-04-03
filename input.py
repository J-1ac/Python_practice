number = int(input("숫자를 입력하시오\n"))   #input은 str타입, 형변환 시켜줌.

result = 1                                  #초기 변수값
i = 1

while i < number :
    result = result * i
    i = i+1                                 #반복문으로 팩토리얼 계산
    

print(number, "! =", result, " 입니다.")     #결과 출력