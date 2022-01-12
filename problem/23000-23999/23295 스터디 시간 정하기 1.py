from itertools import accumulate
import sys


N, T = map(int, input().split())
time = [0] * 100001
for _ in range(N):
    K = int(next(sys.stdin))
    for _ in range(K):
        s, e = map(int, next(sys.stdin).split())
        time[s] += 1
        time[e] -= 1

time = [0] + list(accumulate(accumulate(time)))

maxtime = max(range(100001 - T), key=lambda x: time[x + T] - time[x])
print(maxtime, maxtime + T)
