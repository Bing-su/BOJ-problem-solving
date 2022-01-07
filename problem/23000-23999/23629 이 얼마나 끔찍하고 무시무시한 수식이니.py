import re
from operator import add, sub, mul

div = lambda x, y: int(x / y)  # c++와 같은 방식의 정수 나눗셈
s = r"ZERO|ONE|TWO|THREE|FOUR|FIVE|SIX|SEVEN|EIGHT|NINE"
s2n = dict(zip(s.split("|"), "0123456789"))
n2s = {v: k for k, v in s2n.items()}
func = {"+": add, "-": sub, "x": mul, "/": div}

expr = re.sub(s, lambda m: s2n[m.group()], input())
arr = re.split(r"([+\-x/])", expr[:-1])

try:
    num = int(arr[0]) if arr[0] else 0
    for i in range(1, len(arr), 2):
        num = func[arr[i]](num, int(arr[i + 1]))
except ValueError:
    print("Madness!")
else:
    print(expr)
    print(re.sub(r"\d", lambda m: n2s[m.group()], str(num)))
