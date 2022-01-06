# 23885 비숍 투어
N, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print("YES" if a == b or N > 1 and M > 1 and sum(a) % 2 == sum(b) % 2 else "NO")
