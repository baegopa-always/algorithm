def sol(w):
	if table[w] != w:
		table[w] = sol(table[w])
	else:
		return w
	return table[w]
 
t = 0
n, m = map(int,input().split())
table = [i for i in range(n+1)]
tree = []
for _ in range(m):
    u, v, w = map(int,input().split())
    w=0-w
    tree.append((w, u, v))
    t += w

s = 0
tree.sort()
for w, u, v in tree:
    u, v = sol(u), sol(v)
    if u!=v:
        s += w
        table[max(u,v)] = min(u,v)

print(abs(t - s))