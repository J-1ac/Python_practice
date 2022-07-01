a, b, v = map(int, input().split())
if a>=v:
    print("1")
elif (v-a)<=(a-b):
    print("2")
else:
    print(int((v-b-1)//(a-b) +1))