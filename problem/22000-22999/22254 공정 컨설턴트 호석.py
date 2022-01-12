from heapq import heappop, heappush


def solve(n):
    heap = [0] * n
    for t in time:
        heappush(heap, heappop(heap) + t)
    return max(heap) <= X


N, X = map(int, input().split())
time = list(map(int, input().split()))
low, high = 1, N

while low < high:
    mid = (low + high) // 2

    if solve(mid):
        high = mid
    else:
        low = mid + 1

print(high)
