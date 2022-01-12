import sys


for _ in range(int(input())):
    query = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())
    arr = eval(sys.stdin.readline())

    lp, rp, d = 0, n, 1

    for q in query:
        if q == "R":
            d *= -1
        elif d == 1:
            lp += 1
        else:
            rp -= 1

    if lp > rp:
        print("error")
    else:
        print(f"{arr[lp:rp][::d]}".replace(" ", ""))
