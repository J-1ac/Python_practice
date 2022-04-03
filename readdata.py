f = open("data.txt", "r")
while True:
    line = f.readline()
    if not line : break             #readline()은 더 이상 읽을 줄이 없으면 none 출력
    print(line)
f.close()