# 23972 악마의 제안
K, N = map(int, input().split())
if N == 1:
    print(-1)
else:
    print(-(-N * K // (N - 1)))
