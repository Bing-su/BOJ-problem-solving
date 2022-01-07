import sys


def find(n: int) -> int:
    if parent[n] != n:
        parent[n] = find(parent[n])
    return parent[n]


def union(u: int, v: int):
    if rank[u] < rank[v]:
        parent[u] = v
        exits[v] = min(exits[u], exits[v])
        exits[u] = 0
    else:
        parent[v] = u
        exits[u] = min(exits[u], exits[v])
        exits[v] = 0
        if rank[u] == rank[v]:
            rank[u] += 1


input = sys.stdin.readline
N, M = map(int, input().split())
parent = list(range(N + 1))
rank = [0] * (N + 1)
edges = []

for _ in range(M):
    u, v, c = map(int, input().split())
    edges.append((c, u, v))
edges.sort()
exits = [0] + list(map(int, input().split()))
warp = 0

for c, u, v in edges:
    u, v = find(u), find(v)
    if u != v and (c <= exits[u] or c <= exits[v]):
        union(u, v)
        warp += c

print(sum(exits) + warp)


# 다른 풀이, 코드는 더 짧지만 시간은 더 걸렸음 (496ms -> 940ms)
import sys


def find(n):
    if parent[n] != n:
        parent[n] = find(parent[n])
    return parent[n]


def union(u, v):
    if rank[u] < rank[v]:
        parent[u] = v
    else:
        parent[v] = u
        if rank[u] == rank[v]:
            rank[u] += 1


input = sys.stdin.readline
N, M = map(int, input().split())
parent = list(range(N + 1))
rank = [0] * (N + 1)
edges = []

for _ in range(M):
    u, v, c = map(int, input().split())
    edges.append((c, u, v))
for i, c in enumerate(map(int, input().split()), 1):
    edges.append((c, i, 0))
edges.sort()

cost = 0
for c, u, v in edges:
    u, v = find(u), find(v)
    if u != v:
        union(u, v)
        cost += c

print(cost)
