import sys
T=int(sys.stdin.readline())
for _ in range(T):
    def sol():
        x, w=map(int,sys.stdin.readline().split())
        count=0
        while x<w:
            x*=2
            count+=1
        print(count)
    sol()