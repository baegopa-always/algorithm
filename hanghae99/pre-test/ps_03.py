import sys
input = sys.stdin.readline

def dfs_for_pre(node):
    if node == '.':
        return
    answer.append(node)
    dfs_for_pre(nodes[node][0])
    dfs_for_pre(nodes[node][1])
    return

def dfs_for_mid(node):
    if node == '.':
        return
    dfs_for_mid(nodes[node][0])
    answer.append(node)
    dfs_for_mid(nodes[node][1])
    return

def dfs_for_post(node):
    if node == '.':
        return
    dfs_for_post(nodes[node][0])
    dfs_for_post(nodes[node][1])
    answer.append(node)
    return

n = int(input())
nodes = {}
for _ in range(n):
    node = list(input().rstrip().split())
    nodes[node[0]] = node[1], node[2]

answer = []
dfs_for_pre('A')
print(*answer,sep="")

answer = []
dfs_for_mid('A')
print(*answer,sep="")

answer = []
dfs_for_post('A')
print(*answer,sep="")