import sys
input = sys.stdin.readline
n = int(input())
checkin = {}
for _ in range(n):
    name, status = input().split()
    if status == "enter":
        checkin[name] = 1
    else:
        checkin[name] = 0
ans = []
for name, status in checkin.items():
    if status == 1:
        ans.append(name)
for x in sorted(ans, reverse=True):
    print(x)