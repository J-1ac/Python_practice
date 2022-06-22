T=int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    room=[0,0]
    if H!=1:
        if N%H==0:
            room[0]=H
            room[1]=N//H
        else:
            room[0]=N%H
            room[1]=N//H+1
    else:
        room[0]=1
        room[1]=N
    print(room[0],end="")
    if room[1]<10:
        print(f"0{room[1]}")
    else:
        print(room[1])