import copy
# copy or cloning
l1=[10,20,30,40]
l2=l1.copy()
# l2[2]=70
l1[2]=70
print("l1:", l1)
print("l2:", l2)

# Shallow copy, if nested mutable objects are in l1, l1 changes will reflect to l2 for only mutable object set.
# if there is not nested mutable objects, l2 remains completely back-up for original data, l1 changes happen.
l1=[10,20,[30,40], 50]
l2=copy.copy(l1)
l1[0]=111
l1[1]=222
l1[2][0]=888
l2[2][1]=999
print("l1:", l1)
print("l2:", l2)

# Deepcopy l2 complete back-up for l1, even if we are changing in l1, these not refelct to l2.
l1=[10,20,[30,40], 50]
l2=copy.deepcopy(l1)
l1[0]=111
l1[1]=222
l1[2][0]=888
l1[2][1]=999
l1[3]=777
print("l1:", l1)
print("l2:", l2)