def dday(date1, date2):
    if date1[0] + 1000 < date2[0]:
        return print("gg")
    elif date1[0] + 1000 == date2[0] and date1[1] <= date2[1] and date1[2] <= date2[2]:
        return print("gg")
    day1, day2 = 0, 0
    for year in range(1, date1[0]):
        if year%400==0:
            day1+=366
        elif year%100==0:
            day1+=365
        elif year%4==0:
            day1+=366
        else:
            day1+=365
    for year in range(1, date2[0]):
        if year%400==0:
            day2+=366
        elif year%100==0:
            day2+=365
        elif year%4==0:
            day2+=366
        else:
            day2+=365
    for month in range(1, date1[1]):
        if month in [1, 3, 5, 7, 8, 10, 12]:
            day1+=31
        elif month in [4, 6, 9, 11]:
            day1+=30
        else:
            if date1[0]%400==0:
                day1+=29
            elif date1[0]%100==0:
                day1+=28
            elif date1[0]%4==0:
                day1+=29
            else:
                day1+=28
    for month in range(1, date2[1]):
        if month in [1, 3, 5, 7, 8, 10, 12]:
            day2+=31
        elif month in [4, 6, 9, 11]:
            day2+=30
        else:
            if date2[0]%400==0:
                day2+=29
            elif date2[0]%100==0:
                day2+=28
            elif date2[0]%4==0:
                day2+=29
            else:
                day2+=28
    day1+=date1[2]
    day2+=date2[2]
    return print(f"D-{day2-day1}")            

d1 = list(map(int, input().split()))
d2 = list(map(int, input().split()))

dday(d1, d2)