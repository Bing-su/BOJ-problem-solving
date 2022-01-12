import sys
from heapq import heappop, heappush


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for i, line in enumerate(sys.stdin):
    u, v = map(int, line.split())
    graph[u].append((v, i))
    graph[v].append((u, i))

dist = [float("inf")] * (N + 1)
dist[1] = 0

queue = [(0, 0, 1)]
while queue:
    d, f, n = heappop(queue)

    if d > dist[n]:
        continue

    for adj, nf in graph[n]:
        nd = d + (nf - f) % M + 1
        if nd < dist[adj]:
            dist[adj] = nd
            heappush(queue, (nd, (nf + 1) % M, adj))

print(dist[N])
