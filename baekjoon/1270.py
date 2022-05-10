def consider_occupy(list_land):
    population = list_land[0]
    land = list_land[0:]
    for i in range(population):
        count = land.count(land[i])
        if count > int(population/2):
            return print(land[i])
    return print("SYJKGW")

T = int(input())
for _ in range(T):
    land = list(map(int, input().split(" ")))
    consider_occupy(land)