import math
x, y, w, s = map(int, input().split())

time=0
if s >= w*2:
    time+=(x+y)*w
elif s < w:
    if x>y:
        time+=y*s
        if (x-y)%2==0:
            time+=(x-y)*s
        else:
            time+=(x-y-1)*s+w
    elif x<y:
        time+=x*s
        if (y-x)%2==0:
            time+=(y-x)*s
        else:
            time+=(y-x-1)*s+w
    else:
        time+=x*s

else:
    if x>y:
        time+=y*s
        time+=(x-y)*w
    elif x<y:
        time+=x*s
        time+=(y-x)*w
    else:
        time+=x*s

print(time)