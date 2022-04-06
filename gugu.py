#gugu.py

def gugu(dan):
    gugu_list =[]
    for i in range(9):
        gugu_list.append((i+1)*dan)
    return gugu_list

dan = int(input("원하는 단을 입력해주세요 :"))
print(gugu(dan))