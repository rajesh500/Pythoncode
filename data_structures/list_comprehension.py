s=[x for x in 'Rajesh J']
print(s)
s=[1,2,3,5,6,7]
a=[y*y for y in range(1, len(s)+2)]
print(a)

b=[[1,2],[2,3],[4,5],[6,7]]
c=[]
h=[]
e=0
for i in range(4):
    d=b[i][e]
    c.append(d)
e=e+1
g=1
for j in range(4):
    f=b[j][g]
    h.append(f)
g=g+1
print(c)
print(h)
print(c+h)
