word="mississippi"
d={}
for x in word:
    # get is method to access key and values, here we are doing increment the values by +1
    d[x]=d.get(x,0)+1
print(d)
for k,v in d.items():
    print(k,"occurred ",v," times")

# Here, keys cannot be duplicate, but values can be duplicated. so, we picked dictionary concept to count the characters

