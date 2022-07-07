L=int(input())
inputstr=input()
H=0
for i in range(len(inputstr)):
    H+=(ord(inputstr[i])-96)*(31**i)
print(H%1234567891)