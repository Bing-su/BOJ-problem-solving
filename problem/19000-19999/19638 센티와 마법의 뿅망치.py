import heapq, sys


N, H, T = map(int, input().split())
height = sorted(map(lambda x: -int(x), sys.stdin))

for t in range(T):
    if -height[0] < H:
        print(f"YES\n{t}")
        break

    h = -heapq.heappop(height)
    if h > 1:
        h //= 2
    heapq.heappush(height, -h)

else:
    if -height[0] < H:
        print(f"YES\n{T}")
    else:
        print(f"NO\n{-height[0]}")
