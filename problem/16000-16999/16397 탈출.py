def button_B(n: int) -> int:
    n *= 2
    n -= 10 ** (len(str(n)) - 1)
    return max(n, 0)


N, T, G = map(int, input().split())
v = [-1] * 100000
v[N] = 0
queue = [N]

for _ in range(T):
    nqueue = []
    for n in queue:
        if n < 99999 and v[n + 1] == -1:
            v[n + 1] = v[n] + 1
            nqueue.append(n + 1)

        if n < 50000 and v[(nb := button_B(n))] == -1:
            v[nb] = v[n] + 1
            nqueue.append(nb)
    queue = nqueue

print(v[G] if v[G] != -1 else "ANG")
