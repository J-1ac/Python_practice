#gugu_practice.py

def gugu(dan):
    i=0
    result = []
    for i in range(9):
        result.append((i+1)*dan)
    print(result)

n = int(input("plz input ur dan :"))
gugu(n)