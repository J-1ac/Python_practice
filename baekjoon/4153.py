while True:
    sides = list(map(int, input().split()))
    if sides[0]==0 and sides[1]==0 and sides[2]==0:
        break
    hypotenus=0
    for i in range(3):
        if hypotenus<sides[i]:
            hypotenus=sides[i]
    sides.remove(hypotenus)
    if hypotenus**2 == sides[0]**2 + sides[1]**2:
        print("right")
    else:
        print("wrong")