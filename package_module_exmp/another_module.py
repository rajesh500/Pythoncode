# import package_module_exmp.module as m   # alias, alias name we have to use
# m.add(100, 200

#  ^
#  |
#  |
# re-using code from module.py, whenever, i am calling add method from another_module to module all the methods are executing, I want explicitly only one method.
# m.add(100, 200) # by calling module.py, add method all the methods are executing and what ever code written in module.py and passing argument to those method
# it should execute with in that module only, it should not execute in another module. so, to get that if__name__=='__main__':



from package_module_exmp.module import a, add as m
from random import *

m(100, 200)
print(a)   # variable accessing
print(dir())   # display all the methods( include inbuilt methods) available in current module


# random number generation
for i in range(10):
    # print(random())    # generate 10 float value between 0 to 1
    # print(randint(1, 100))
    print(uniform(1,100))  # given number are not inclusive



# randrange & range() both are same.