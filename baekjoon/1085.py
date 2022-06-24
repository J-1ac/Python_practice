x, y, w, h = map(int, input().split())
dcases=[x, y, w-x, h-y]
print(min(dcases))