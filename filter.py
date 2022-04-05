#filter.py / compare with positive.py

def positive(x):
    return x > 0

print(list(filter(positive, [1,-3,2,0,-5,6])))      #filter() / 첫번째 인수(함수) 값 참만을 묶어서 return해줌

#list(filter(lambda x: x > 0, [1,-3,2,0,-5,6]))     #lambda 사용