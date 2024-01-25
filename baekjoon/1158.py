import sys
input = sys.stdin.readline

n,k = map(int,input().split())
people = [i+1 for i in range(n)]
c = 0
ans = []
while people:
    c=(c-1+k) % len(people)
    ans.append(people[c])
    del people[c]
print("<",end="")
print(*ans,sep=", ",end="")
print(">")