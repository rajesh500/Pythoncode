# Frozenset, is exactly same as set but only difference is immutable.
# Mostly frozenset is used for key in dictionary.

t=(10,20,30,40,50,60,70,80)
f=frozenset(t)
print(f)


dictic={"Name":"Rajesh",  "Last":"Jak", "Country":"USA", "Age":26}
keys=frozenset(dictic)   # it retrieve all the keys in Dictionary
print(keys)