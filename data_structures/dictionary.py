# empty dictionary
# 1)
d={}
# 2)
d1=dict()

# dictionary data set
d2={100:"Rajesh", 200:"Jak", 300:"Python", 400:"USA"}
# accessing value
print(d2[100])
# adding or updating the value
d2[500]="Cog"
print(d2)
# deletig the value
del d2[500]
# removing value
print(d2.pop(400))   # remove the value and display that value, if the key is not available it will return error.
print(d2)
# list of keys in dictionary data set
print(d2.keys())
# list of values in dictionary data set
print(d2.values())
# length
print(len(d2))
# get the value with key or key, value
print(d2.get(200))   # if key is available it returns corresponding value, otherwise none,it won't raise any error.
print(d2.get(300, "Python"))
print("------------:", d2)
# If the key is already available then this function returns the corresponding value
# If the key is not available then the specified key-value will be added as new item to the dictionary
print(d2.setdefault(400, "USA"))
print(d2)
# adding value to empty data set.
d[10]="Raj"
print(d)
# adding two dictionary data sets.
d2.update(d)
print(d2)