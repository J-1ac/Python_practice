#sumofinput.py

a = input().split(",")
sum=0

for i in a:
    sum += int(i)

print(sum)