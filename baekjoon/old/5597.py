x=[i+1 for i in range(30)]
for _ in range(28):
    x.remove(int(input()))
print(*x,sep="\n")