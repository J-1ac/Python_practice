hour, min = map(int, input().split())
if min>=45:
    print(hour, min-45)
else:
    if hour>=1:
        print(hour-1, min+60-45)
    else:
        print(23, min+60-45)