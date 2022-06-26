T=int(input())
for _ in range(T):
    k=int(input())
    n=int(input())
    previous_rooms=list(range(1,n+1))
    count=0
    while count<k:
        new_rooms=[]
        new_rooms.append(1)
        for i in range(1,n):
            new_rooms.append(new_rooms[i-1]+previous_rooms[i])
        previous_rooms=new_rooms
        count+=1
    print(previous_rooms[n-1])