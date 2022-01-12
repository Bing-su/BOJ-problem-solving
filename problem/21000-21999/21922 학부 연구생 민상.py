from itertools import product


def search(i, j, d):
    while True:
        i, j = i + dy[d], j + dx[d]
        if not (0 <= i < N and 0 <= j < M) or arr[i][j] == 9:
            break

        v[i][j] = 1

        if arr[i][j] == 1 and d in (0, 2) or arr[i][j] == 2 and d in (1, 3):
            break
        elif arr[i][j] == 3:
            d = 3 - d
        elif arr[i][j] == 4:
            d ^= 1


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
v = [[0] * M for _ in range(N)]
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]


for i, j in product(range(N), range(M)):
    if arr[i][j] == 9:
        v[i][j] = 1
        for d in range(4):
            search(i, j, d)

print(sum(map(sum, v)))
