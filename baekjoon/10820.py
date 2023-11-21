import sys

for line in sys.stdin:
    ans = [0] * 4
    for x in line:
        if 'a' <= x <= 'z':
            ans[0] += 1
        elif 'A' <= x <= 'Z':
            ans[1] += 1
        elif '0' <= x <= '9':
            ans[2] += 1
        elif x == ' ':
            ans[3] += 1
    print(*ans)
