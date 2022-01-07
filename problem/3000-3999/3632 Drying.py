N = int(input())
A = tuple(map(int, input().split()))
K = int(input()) - 1

low, high = 1, max(A)

if not K:
    print(high)
    raise SystemExit

while low < high:
    mid = (low + high) // 2
    a = [max(x - mid, 0) for x in A]
    time = sum(-(-x // K) for x in a)  # math.ceil과 같은 연산

    if time > mid:
        low = mid + 1
    else:
        high = mid

print(high)
