#average.py

f = open("sample.txt", "r")
lines = f.readlines()
f.close()

sum=0
for line in lines:
    sum += int(line)

average = sum / len(lines)

print("sum :", sum)
print("average :", average)


f = open("result.txt", "w")
f.write(str(sum)+"\n")
f.write(str(average))
f.close()