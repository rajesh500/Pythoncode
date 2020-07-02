# empty set
s=set()
print(type(s))

# conversions
# List to set, set to List, tuple to set, set to tuple
l=[1,2,3]
t=(4,5,6,5,6,3,4,5,3,2,3,4)
s={10,11,12,13,14,15,16,10,13,12}
a=set(l)
print(type(a))
b=list(s)
print(type(b))
c=set(t)
print(type(c))
print(c) # duplicate are not allowed
d=tuple(s)
print(type(d))

#
ss=set(range(1, 10, 2))
print(ss)

# adding element to set(s)
s.add(19)
print(s)
s.update(l, range(3))
print(s)

sss=s.copy()
print(sss)
ll=[100,200]
sss.update(ll, range(2))
print(sss)

print(s.difference(sss)) #  or print(s-sss)
print(s.union(sss))  # or print(s|sss)
print(s&sss)  # or print(s.intersection(sss))
print(s^sss)  # or   print(s.symmetric_difference(sss))
ssss={300,400}
print(sss.symmetric_difference_update(ssss))


# set comprehension

z={ x*x for x in range(1,5)}
print(z)

aa="Rajesh"
cc="Jak"
bb=set(aa)
dd=set(cc)
print(bb)
print(dd)
print(bb&dd)

# s={10,11,12,13,14,15,16,10,13,12}
s.pop()
print(s)