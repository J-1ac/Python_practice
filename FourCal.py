class FourCal:
    def __init__(self, first, second):              #생성자
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second
    
    def add(self):
        return self.first + self.second

    def sub(self):
        return self.first - self.second

    def mul(self):
        return self.first * self.second

    def div(self):
        return self.first / self.second

class MoreFourCal(FourCal):                         #상속 class
    def pow(self):
        return self.first ** self.second

class SafeFourCal(FourCal):                         #method overriding
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second



a = SafeFourCal(4,0)

print(a.add())
print(a.sub())
print(a.mul())
print(a.div())
#print(a.pow())


"""
x = int(input("숫자1 입력 : "))
y = int(input("숫자2 입력 : "))

a = FourCal()
a.setdata(x, y)

print("두 숫자의 합 :", a.add())
print("두 숫자의 차 :", a.sub())
print("두 숫자의 곱 :", a.mul())
print("두 숫자의 몫 :", a.div()) """