def cal_k(X, Y):
    Z = int(Y * 100 / X)
    if X==Y or Z >= 99:
        return -1
    l1 = X*Z + X - 100*Y
    l2 = 99-Z
    k = int(l1/l2)
    if l1 % l2 != 0:
        return k + 1
    else:
        return k

X, Y = map(int, input().split(" "))
print(cal_k(X, Y))