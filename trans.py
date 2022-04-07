#trans.py

f1 = open("abc.txt", "r")
content = f1.readlines()
f1.close()
content.reverse()

f2 = open("abc.txt", "w")
for line in content:
    line = line.strip()
    f2.write(line)
    f2.write("\n")
f2.close()

