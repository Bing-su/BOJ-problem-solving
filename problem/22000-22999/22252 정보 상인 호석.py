from collections import defaultdict
from heapq import heappop, heappush
import sys


input()
d = defaultdict(list)
ans = 0

for line in sys.stdin:
    q, name, *nums = line.split()
    if q == "1":
        for n in map(int, nums[1:]):
            heappush(d[name], -n)
    else:
        n = int(nums[0])
        for _ in range(min(n, len(d[name]))):
            ans -= heappop(d[name])

print(ans)
