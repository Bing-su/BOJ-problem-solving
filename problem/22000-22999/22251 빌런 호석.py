from itertools import product


a = [119, 18, 93, 91, 58, 107, 111, 82, 127, 123]
c = [[0] * 10 for _ in range(10)]
for i, j in product(range(10), repeat=2):
    c[i][j] = bin(a[i] ^ a[j]).count("1")


N, K, P, X = map(int, input().split())
Y = list(map(int, str(X).zfill(K)))

ans = 0
for f in range(1, N + 1):
    idx = map(int, str(f).zfill(K))
    if 1 <= sum(c[v][i] for v, i in zip(Y, idx)) <= P:
        ans += 1

print(ans)
