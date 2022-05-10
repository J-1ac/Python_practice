import sys
from collections import Counter

def consider_occupy(list_info):
    population = list_info[0]
    land = list_info[0:]
    count = Counter(land)
    for i in range(population):    
        if count[land[i]] > population/2:
            return print(land[i])
    return print("SYJKGW")

T = int(input())
for _ in range(T):
    infomation = list(map(int, sys.stdin.readline().split()))
    consider_occupy(infomation)