from heapq import heappop, heappush


N, M = map(int, input().split())
si, sj, ei, ej = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
v = [[[False] * 3 for _ in range(M)] for _ in range(N)]

dd = [[(1, 0), (0, 1), (-1, 0), (0, -1)], [(0, 1), (0, -1)], [(1, 0), (-1, 0)]]
queue = [(0, si - 1, sj - 1, 1)]

while queue:
    impact, i, j, m = heappop(queue)

    if v[i][j][m]:
        continue

    if i == ei - 1 and j == ej - 1:
        print(impact)
        break

    v[i][j][m] = True
    nm = (m + 1) % 3

    for dx, dy in dd[m]:
        ni, nj = i + dy, j + dx

        if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] != -1 and not v[ni][nj][nm]:
            nimpact = impact + arr[ni][nj]
            heappush(queue, (nimpact, ni, nj, nm))
else:
    print(-1)
