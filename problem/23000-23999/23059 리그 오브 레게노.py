import sys
from collections import defaultdict


input()
degree, graph = defaultdict(int), defaultdict(list)
items = set()

for line in sys.stdin:
    a, b = line.split()
    graph[a].append(b)
    degree[b] += 1
    items.update((a, b))

queue = [item for item in items if not degree[item]]
answer = sorted(queue)

while queue:
    nqueue = []
    for n in queue:
        for adj in graph[n]:
            degree[adj] -= 1
            if degree[adj] == 0:
                nqueue.append(adj)
    answer += sorted(nqueue)
    queue = nqueue

if len(answer) == len(items):
    print("\n".join(answer))
else:
    print(-1)

# 다른 풀이, python 3.9에 추가된 기능
from graphlib import TopologicalSorter
import sys


graph = TopologicalSorter()
input()
for line in sys.stdin:
    a, b = line.split()
    graph.add(b, a)

try:
    graph.prepare()
except:
    print(-1)
else:
    while graph.is_active():
        r = sorted(graph.get_ready())
        print("\n".join(r))
        graph.done(*r)
