def convexHull(state):
    cvList = []
    for k in state:
        while len(cvList) >= 2:
            i, j = cvList[-1], cvList[-2]
            p, q = [], []
            for r in range(2):
                p.append(i[r] - j[r])
                q.append(k[r] - i[r])
            if p[0] * q[1] > p[1] * q[0]:
                break
            cvList.pop()
        cvList.append(k)
    return len(cvList)-1

n, m = map(int,input().split())
state = []
for i in range(m):
    state.append(list(map(int, input().split())))
state.sort(key=lambda x:x[0:1])
print(convexHull(state) + convexHull(reversed(state)))