ab = [100, ['Python', 'is', 'a', 50], ['very', 'good', 'programming'], ['language', 'in', 'the', 'world'], 2020]
#print(ab)
#print(ab[0][1])
print(ab[1][2])
print(ab[1][-1])
print(ab[4])
#print(ab[3])
c=ab[3]
print(c)
#for i in range(len(c)):
  #print(c[i])

a=[1,2,3,2,3,4,4,3,2,3,4,33]
b=[4,5,6]
print(a+b)
#print(ab[1]+ab[2])
##print(ab[2]+ab[3])
d=ab.append(2019)
print(ab)
x=a.clear()
print(a)
print(x)   # every operation is happening in the list not in variable
a=b.copy()
print(a)
print(a.count(4))

'''
append()	Adds an element at the end of the list
clear()   	Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	    Sorts the list 
max()
min()
......
'''