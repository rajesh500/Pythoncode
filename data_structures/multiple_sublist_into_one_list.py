b=[[1,2],[2,3],[4,5],[6,7]]
c=[]
h=[]
e=0

# for i in range(4)
for i in range(len(b)):
    d=b[i][e]
    c.append(d)
e=e+1
g=1

# for j in range(4):
for j in range(len(b)):
    f=b[j][g]
    h.append(f)
g=g+1
print(c)
print(h)
print(c+h)


# 2) way

