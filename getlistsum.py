#getlistsum.py

def PASS(l):
    sum = 0
    for i in l:
        if i > 50:
            sum += i 
    return sum

A = [20,55,67,82,45,33,90,87,100,25]
print("sum :", PASS(A))