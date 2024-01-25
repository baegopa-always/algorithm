def convex_hull(positions):
    convex = []
    for p3 in positions:
        while len(convex) >= 2:
            p1, p2 = convex[-2], convex[-1]
            v = p2[0] - p1[0], p2[1] - p1[1]
            u = p3[0] - p2[0], p3[1] - p2[1]
            if v[0] * u[1] > v[1] * u[0]:
                break
            convex.pop()
        convex.append(p3)
    return len(convex)-1
 
n, m = map(int,input().split())
answer = 0
positions = []
for i in range(m):
    positions.append(list(map(int, input().split())))
positions.sort(key=lambda pos:(pos[0], pos[1]))
answer += convex_hull(positions)
answer += convex_hull(reversed(positions))
print(answer)