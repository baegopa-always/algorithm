s,t=0,0
for i in range(20):
    a,b,c=input().split()
    if c[0]=="P":
        continue
    b=float(b)
    s+=b
    if c[0]=="A":
        t+=4*b
    elif c[0]=="B":
        t+=3*b
    elif c[0]=="C":
        t+=2*b
    elif c[0]=="D":
        t+=1*b
    if len(c)>1:
        if c[1]=="+":
            t+=0.5*b
print("{:.6f}".format(t/s))