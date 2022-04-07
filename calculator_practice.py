#calculator_practice.py

class Calculator:
    def __init__(self, numberList):
        self.numberList = numberList

    def sum(self):
        sum = 0
        for num in self.numberList:
            sum += num
        return sum
    def avg(self):
        return self.sum()/len(self.numberList)

cal1 = Calculator([1,2,3,4,5])
cal2 = Calculator([6,7,8,9,10])

print(cal1.sum())
print(cal1.avg())
print(cal2.sum())
print(cal2.avg())