def compare(eleclist):
    count=0
    if len(eleclist) == 1 or eleclist.index(max(eleclist)) == 0:
        return print("0")
    else:
        for i in range(1,len(eleclist)):
            while eleclist[0] <= eleclist[i]:
                eleclist[0], eleclist[i] = eleclist[0]+1, eleclist[i]-1
                count += 1
        if eleclist.index(max(eleclist)) != 0:
            return print(count+1)
        else:
            return print(count)
    


N = int(input())
election_list =[]

for _ in range (N):
    election_list.append(int(input()))

compare(election_list)
