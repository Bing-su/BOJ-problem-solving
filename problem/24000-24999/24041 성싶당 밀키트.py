import sys

N, G, K = map(int, input().split())
A = [[], []]
for line in sys.stdin:
    s, l, o = map(int, line.split())
    A[o].append((s, l))

low, high = 1, 2 * 10 ** 9
while low <= high:
    mid = (low + high) // 2

    t = sum(s * max(1, mid - l) for s, l in A[0])
    nim = [s * max(1, mid - l) for s, l in A[1]]
    nim.sort(reverse=True)
    t += sum(nim[K:])

    if t > G:
        high = mid - 1
    else:
        low = mid + 1

print(high)
