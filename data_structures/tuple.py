# Data
t=10,20,30,40
t1=(10,20,30,40)
# single variable tuple
t2=50,
# empty tuple
t3=()
# heterogenous data
tt=(10,20,('A', 30), 'B')
print(t)
print(type(t))
print(t1)
print(type(t1))
print(t2)
print(type(t2))
print(type(t3))
# accessing tuple data
print(t[0])
# negative index
print(t[-1])
# slicing
print(t[2:4])
# adding tuple
print(t1+t2)
# accessing nested tuple
print(tt[2][1])
# del t3
# print(t3)
# tuple comprehension is not there
p=(x*x for x in range(len(t1)))
print(p)

# tuple to string conversation
t=('U', 'S', 'A', 'A', 'M', 'E', 'R')
p=''.join(t)
print(t)
print(type(t))
print(p)
print(type(p))
# index
for i in range(len(t)):
  print(t[i], "index is", i)
print(t.index("A"))

# tuple to list
x=list(t)
y=[]

# list to tuple
z=tuple(x)

# appending and removing is not there in tuple, because it is immutbale

# packing and unpacking
a=10
b=20
c=30
m=a,b,c
print(m)
print(type(m))
n=100,200,300
d,e,f=n
print(d,e,f)
print(type(d))