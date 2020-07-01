# 1)
s="This is the example of loop"
t=s.split()
u=list(reversed(t))
v=' '.join(u)
print(v)

# b=' '.join(reversed(m))
# print(b)

# 2)
for i in reversed(t):
    print(i, end=' ')

# 3)
a="This is the example of loop and standard"
b=a.split()
for i in reversed(b):
  print(i[::-1])