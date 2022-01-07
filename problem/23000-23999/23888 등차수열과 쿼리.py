import sys
from math import gcd


def seq_sum(a: int, d: int, n: int) -> int:
    return n * (2 * a + (n - 1) * d) // 2


a, d = map(int, input().split())
input()
g = gcd(a, d)
for line in sys.stdin:
    x, l, r = map(int, line.split())
    if x == 1:
        print(seq_sum(a + d * (l - 1), d, r - l + 1))
    elif l == r:
        print(a + d * (l - 1))
    else:
        print(g)
