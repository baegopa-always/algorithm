import sys

def countExp(n,t):
    c = 0
    while n:
        n//=t
        c+=n
    return c

input = sys.stdin.readline
a,b = map(int,input().split())

print(min(countExp(a,2)-countExp(a-b,2)-countExp(b,2), countExp(a,5)-countExp(a-b,5)-countExp(b,5)))