from itertools import chain, groupby


def blizzard(d: int, r: int) -> None:
    dx, dy = [0, 0, 0, -1, 1], [0, -1, 1, 0, 0]
    i = j = N // 2
    for _ in range(r):
        i, j = i + dy[d], j + dx[d]
        arr[i][j] = 0


def explode() -> list[list[int, int]]:
    global answer

    nums = [arr[i][j] for i, j in points if arr[i][j]]
    remain = [[len(list(g)), n] for n, g in groupby(nums)]
    boomed = False

    while True:
        temp, nxt = [], []
        for c, n in remain:
            if c > 3:
                answer += n * c
                boomed = True
            else:
                temp.append([c, n])

        if not boomed:
            return temp

        for n, g in groupby(temp, key=lambda x: x[1]):
            s = sum(x[0] for x in g)
            nxt.append([s, n])

        remain = nxt
        boomed = False


def transform() -> None:
    for n, (i, j) in zip(chain.from_iterable(remain), points):
        arr[i][j] = n


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = 0

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
i = j = N // 2
points = []

d = 0
for a in range(2, N * 2 + 1):
    for _ in range(a // 2):
        i, j = i + dy[d], j + dx[d]
        points.append((i, j))
    d = (d + 1) % 4

points.pop()

for _ in range(M):
    d, r = map(int, input().split())
    blizzard(d, r)
    remain = explode()
    arr = [[0] * N for _ in range(N)]
    transform()

print(answer)
