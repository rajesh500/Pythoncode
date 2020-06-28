s='abacadbbcd'
c=0
for i in range(len(s)):
    print(s[i])
    a=s[i]
    for j in range(len(s)):
        b=s[j]
        if a==b:
            c+=1
    print(c)