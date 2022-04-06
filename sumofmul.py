#sumofmul.py

def sumofmul(a, b):
    sum = 0
    for i in range(1000):
        if i % a == 0 or i % b == 0:
            sum += i
    return sum

print(sumofmul(3, 5))