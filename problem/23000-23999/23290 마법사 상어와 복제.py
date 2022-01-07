from collections import Counter, deque
from itertools import chain, product


def move_all(fish: Counter) -> Counter:
    moved = Counter()
    smell_set = set(chain.from_iterable(smell))
    for i, j, d in fish:
        ni, nj, nd = move_one(i, j, d, smell_set)
        moved[ni, nj, nd] += fish[i, j, d]
    return moved


def move_one(i: int, j: int, d: int, smell: set) -> tuple[int, int, int]:
    for m in range(8):
        nd = (d - m) % 8
        ni, nj = i + d8y[nd], j + d8x[nd]

        if (
            (ni < 1 or nj < 1 or ni > 4 or nj > 4)
            or (ni, nj) == (si, sj)
            or (ni, nj) in smell
        ):
            continue
        return ni, nj, nd
    return i, j, d


def count_fishes(i: int, j: int) -> int:
    return sum(fish[i, j, d] for d in range(8))


def shark_move(si: int, sj: int) -> tuple[set, int, int]:
    passed: list[tuple[int, tuple]] = []
    cnt_dict = dict()

    for path in shark_path:
        removed = set()
        i, j, cnt = si, sj, 0
        for d in path:
            i, j = i + d4y[d], j + d4x[d]
            if i < 1 or j < 1 or i > 4 or j > 4:
                break
            removed.add((i, j))
        else:
            cnt = sum(count_fishes(i, j) for i, j in removed)
            passed.append((-cnt, path))
            cnt_dict[path] = (removed, i, j)

    _, max_path = min(passed)
    return cnt_dict[max_path]


M, S = map(int, input().split())
fish = Counter()
for _ in range(M):
    i, j, d = map(int, input().split())
    fish[i, j, d - 1] += 1
si, sj = map(int, input().split())
smell = deque(maxlen=2)
shark_path = tuple(product(range(4), repeat=3))

d8x = [-1, -1, 0, 1, 1, 1, 0, -1]
d8y = [0, -1, -1, -1, 0, 1, 1, 1]
d4x = [0, -1, 0, 1]
d4y = [-1, 0, 1, 0]

for ep in range(S):
    copied = fish.copy()
    fish = move_all(fish)

    removed, si, sj = shark_move(si, sj)
    smell_add = set()
    for (i, j), d in product(removed, range(8)):
        if fish[i, j, d]:
            smell_add.add((i, j))
            del fish[i, j, d]
    smell.append(smell_add)
    fish += copied

print(sum(fish.values()))
