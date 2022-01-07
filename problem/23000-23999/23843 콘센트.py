N, M = map(int, input().split())
queue = [0] * M
for n in sorted(map(int, input().split()), reverse=True):
    i = min(range(M), key=queue.__getitem__)
    queue[i] += n
print(max(queue))
