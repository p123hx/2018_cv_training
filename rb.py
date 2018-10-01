number=int(input())
dict_a=dict()
x=dict()
y=dict()
w=dict()
h=dict()
lit=list()
for i in range(number):
    a=input()
    dict_a[i]=a
    t=a.split()
    x[i]=int(ti[0])
    y[i]=int(ti[1])
    w[i]=int(ti[2])
    h[i]=int(ti[3])
t=list()
def screen1(a):
    ratio=w[a]/h[a]
    if abs(ratio-5)<1:
        pass
    else:
        break    
def screen2(a):
    p_w=(w[a]/2)
    p_h=(h[a]/10)
    if abs(p_w-p_h)<0.1:
        pass
    else:
        break
def screen1(a,b):
    p=dict()
    p[a]=h[a]/10
    p[b]=h[b]/10
    if abs(p[a]-p[b])< 0.5:
        if abs(y[a]*p[a]-y[b]*p[b])<1:
            pass
        else:
            break
    else:
        break
def screen2(a,b):
    if abs(15-distance*p[a])<2:
        pass
    else:
        break
for a in range(1,i+1):

    for b in range(a):
        dx=x[b]-x[a]
        dy=y[b]-y[a]
        p_w=(w[a]/2)
        p_h=(h[a]/10))
        
        if abs(p_w-p_h)>0.1:
            continue
        distance=(dx^2+dy^2)^(1/2)
        screen1(a)
        screen2(a)
        screen1(b)
        screen2(b)
        screen1(a,b)
        screen2(a,b)
        proposion(a,b)=p[a]
        lit.append(proportion(a,b))
        pair(a,b)=dict_a[a]+dict_a[b]
        d=dict()
        dict[proportion(a,b)]=pair(a,b)
short=min(lit)
print(d[short])

        
        
        
