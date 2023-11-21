import sys
input = sys.stdin.readline

n = int(input())
dx, dy = [1,0,-1,0], [0,-1,0,1]

def inrange(x,y):
    if -1 < x < n and -1 < y < n:
        return True
    else:
        return False

bomboni = [input().rstrip() for _ in range(n)]
ans = 1

for i in range(n):
    for j in range(n):
        for k in range(3): # each direction
            count = 1
            for q in range(1,n): # steps
                if inrange(i + dx[k]*q, j + dy[k]*q) and bomboni[i][j] == bomboni[i+dx[k]*q][j+dy[k]*q]:
                    count+=1
                    ans = max(ans,count)
                elif inrange(i + dx[k]*q, j + dy[k]*q) and bomboni[i][j] != bomboni[i+dx[k]*q][j+dy[k]*q]:
                    for p in range(3):
                        if inrange(i+dx[p]+dx[k]*q, j+dy[p]+dy[k]*q) and bomboni[i+dx[p]+dx[k]*q][j+dy[p]+dy[k]*q] == bomboni[i][j]:
                            ans = max(ans,count+1)
                            s = 1
                            for r in range(1,n):
                                if inrange(i + dx[k]*(q+r), j + dy[k]*(q+r)) and bomboni[i][j] == bomboni[i+dx[k]*(q+r)][j+dy[k]*(q+r)]:
                                    ans = max(ans,count+s)
                                    s+=1
print(ans)