# for, if we know number of iteration
# while if you don't know number of iteration we can use it, but we need handle false condition as well other wise loop will keep on running


# 1)   given list we have negative given while loop will work fine
# if there is not negative value then
# List1=[1, 2, 34, 56, 7, 5, 4, 34, -4,-4, -5, -6]
# i=0
# total=0
# while List1[i] >0:
#     total +=List1[i]
#     i+=1
# print(total)


# 2)

# List1=[1, 2, 34, 56, 7, 5, 4, 34]
# i=0
# total=0
# while i < len(List1) and  List1[i] >0 :
#     total += List1[i]
#     i += 1
# print(total)


# 3)

# p=input("Please enter your stirng:")
# for i in p:
#     print(i)
#



# 4)
for i in range(10, 0, -1):  # start, stop-1, step
    print(i)