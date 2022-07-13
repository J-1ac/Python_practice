month,day=map(int,input().split())
while month>1:
    if month-1 in [1, 3, 5, 7, 8, 10, 12]:
        day+=31
        
    elif month-1 in [4, 6, 9, 11]:
        day+=30
    else:
        day+=28   
    month-=1
day-=1
if day%7==0:
    print("MON")
elif day%7==1:
    print("TUE")
elif day%7==2:
    print("WED")
elif day%7==3:
    print("THU")
elif day%7==4:
    print("FRI")
elif day%7==5:
    print("SAT")
else:
    print("SUN")