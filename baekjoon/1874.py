import sys
input = sys.stdin.readline

n = int(input())
result = list(reversed([int(input()) for _ in range(n)]))
s = 1
sub = []
commands = []
while len(result)!= 0:
    if len(sub) > 0 and sub[-1] == result[-1]:
        sub.pop()
        result.pop()
        commands.append("-")
        continue
    elif s <= result[-1]:
        sub.append(s)
        commands.append("+")
    elif len(result) == 0:
        break
    else:
        commands = ["NO"]
        break
    s+=1

for i in commands:
    print(i)