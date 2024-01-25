import sys
n, m = map(int,input().split())
grid = [input() for _ in range(n)]
ans = sys.maxsize

for i in range(n-7):
    for j in range(m-7):
        case1 = 64
        case2 = 64
        for x in range(i,i+8,2):
            for y in range(j,j+8,2):
                if grid[x][y] == "B":
                    case1-=1
                if grid[x+1][y] == "W":
                    case1-=1
                if grid[x][y+1] == "W":
                    case1-=1
                if grid[x+1][y+1] == "B":
                    case1-=1
                if grid[x][y] == "W":
                    case2-=1
                if grid[x+1][y] == "B":
                    case2-=1
                if grid[x][y+1] == "B":
                    case2-=1
                if grid[x+1][y+1] == "W":
                    case2-=1
        ans = min(ans,case1,case2)

print(ans)