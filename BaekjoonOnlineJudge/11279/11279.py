import sys, heapq
input = sys.stdin.readline

N = int(input())

hq = []
for _ in range(N):
    x = int(input())
    
    if x:
        heapq.heappush(hq, -x)
    else:
        if hq:
            print(-heapq.heappop(hq))
        else:
            print(0)
