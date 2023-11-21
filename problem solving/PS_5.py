a,b,c,d,r=map(int,input().split())
t, s = r-abs(a-c), r-(abs(b-d))
print(r*r*2 - t*s if t > 0 and s > 0 else r*r*2)