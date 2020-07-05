word="mynameisrajeshjakandiloveprogramming"
my_chars={'a', 'e', 'i', 'o', 'u'}
d={}
for i in word:
    if i in my_chars:
        d[i]=d.get(i,0)+1
print(d)
for k,v in d.items():
    print(k,"Occured", v, "Times")





